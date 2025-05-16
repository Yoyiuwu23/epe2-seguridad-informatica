#!/usr/bin/env python3
import argparse
import dns.resolver
import whois
import requests
import json
import os
import socket
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from jinja2 import Template

class ReconBot:
    def __init__(self, domain):
        self.domain = domain
        self.api_url = "http://api:8000/analyze/"
        self.report = {
            "metadata": {
                "date": datetime.now().isoformat(),
                "domain": domain,
                "tool": "ReconBot Pro v3.1"
            },
            "dns": {},
            "whois": {},
            "dorks": {},
            "security_analysis": {}
        }

    def run_dns_scan(self):
        records = ['A', 'MX', 'NS', 'SOA', 'TXT']
        resolver = dns.resolver.Resolver()
        resolver.timeout = 5
        resolver.lifetime = 5
        
        for record in records:
            try:
                answers = resolver.resolve(self.domain, record)
                self.report["dns"][record] = [str(r) for r in answers]
            except Exception as e:
                self.report["dns"][record] = f"Error: {str(e)}"

        self.report["security_analysis"]["dns"] = {
            "has_dmarc": any("v=DMARC1" in str(r) for r in self.report["dns"].get("TXT", [])),
            "has_spf": any("v=spf1" in str(r).lower() for r in self.report["dns"].get("TXT", [])),
            "has_secure_ns": any("cloudflare" in ns.lower() or "awsdns" in ns.lower() 
                               for ns in self.report["dns"].get("NS", []))
        }

    def run_whois_lookup(self):
        try:
            w = whois.whois(self.domain)
            self.report["whois"] = {
                "registrar": w.registrar,
                "creation_date": str(w.creation_date),
                "expiration_date": str(w.expiration_date),
                "name_servers": list(w.name_servers) if w.name_servers else [],
                "status": w.status,
                "emails": w.emails if isinstance(w.emails, list) else [w.emails] if w.emails else []
            }
            
            domain_age = (datetime.now() - w.creation_date).days if w.creation_date else 0
            self.report["security_analysis"]["whois"] = {
                "domain_age_days": domain_age,
                "is_expired": w.expiration_date < datetime.now() if w.expiration_date else False,
                "privacy_protection": "PRIVACY" in str(w.status).upper()
            }
        except Exception as e:
            self.report["whois"] = {"error": str(e)}
            self.report["security_analysis"]["whois"] = {"error": "No se pudo obtener información WHOIS"}

    def google_dork(self, query, name):
        try:
            url = f"https://www.google.com/search?q={quote_plus(query)}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            results = []
            for result in soup.select('.g'):
                anchor = result.find('a')
                if anchor:
                    link = anchor.get('href')
                    title = result.find('h3').text if result.find('h3') else 'No title'
                    snippet = result.find('div', {'style': '-webkit-line-clamp:2'})
                    snippet = snippet.text if snippet else 'No description'
                    results.append({
                        "title": title,
                        "url": link,
                        "snippet": snippet
                    })
            
            self.report["dorks"][name] = {
                "query": query,
                "results": results[:5]
            }
            
            if results:
                text_to_analyze = " ".join([r['title'] + " " + r['snippet'] for r in results])
                analysis = self.analyze_with_deepseek(text_to_analyze)
                if analysis:
                    self.report["dorks"][name]["analysis"] = analysis
                    
            return results
            
        except Exception as e:
            self.report["dorks"][name] = {"error": str(e)}
            return []

    def analyze_with_deepseek(self, text):
        try:
            response = requests.post(
                self.api_url,
                json={"text": text[:3000]},
                headers={'Content-Type': 'application/json'},
                timeout=15
            )
            return response.json() if response.status_code == 200 else {"error": f"API status {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

    def generate_security_score(self):
        score = 100
        
        a_records = self.report["dns"].get("A", [])
        if isinstance(a_records, str) and a_records.startswith("Error:"):
            score -= 40
        elif isinstance(a_records, list) and not a_records:
            score -= 20
        
        if not self.report["security_analysis"]["dns"]["has_spf"]:
            score -= 15
        if not self.report["security_analysis"]["dns"]["has_dmarc"]:
            score -= 15
        if any(d.get("results") for d in self.report["dorks"].values()):
            score -= 30
        
        if self.report["security_analysis"]["dns"]["has_secure_ns"]:
            score += 10
        if self.report["security_analysis"]["whois"].get("privacy_protection", False):
            score += 5
            
        return max(0, min(100, score))

    def _generate_html_report(self, filename):
        """Genera un reporte HTML con Jinja2"""
        template = Template('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Reporte - {{ report.metadata.domain }}</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 2em; }
                h1 { color: #2c3e50; }
                .section { background: #f8f9fa; padding: 1em; border-radius: 5px; margin-bottom: 1em; }
                .score { font-size: 1.5em; font-weight: bold; }
                .score-A { color: #27ae60; }
                .score-B { color: #f39c12; }
                .score-C { color: #e67e22; }
                .score-D { color: #d35400; }
                .score-F { color: #c0392b; }
            </style>
        </head>
        <body>
            <h1>Reporte de Seguridad</h1>
            <div class="section">
                <h2>{{ report.metadata.domain }}</h2>
                <p>Fecha: {{ report.metadata.date }}</p>
                <p class="score score-{{ report.security_analysis.rating }}">
                    Puntaje: {{ report.security_analysis.score }}/100 ({{ report.security_analysis.rating }})
                </p>
            </div>

            <div class="section">
                <h2>DNS</h2>
                <pre>{{ report.dns | tojson(indent=2) }}</pre>
            </div>

            <div class="section">
                <h2>WHOIS</h2>
                <pre>{{ report.whois | tojson(indent=2) }}</pre>
            </div>

            {% for name, dork in report.dorks.items() %}
            <div class="section">
                <h3>Dork: {{ name }}</h3>
                <p><strong>Query:</strong> {{ dork.query }}</p>
                {% if dork.results %}
                <ul>
                    {% for result in dork.results %}
                    <li><a href="{{ result.url }}" target="_blank">{{ result.title }}</a> - {{ result.snippet }}</li>
                    {% endfor %}
                </ul>
                {% else %}
                <p>No se encontraron resultados</p>
                {% endif %}
            </div>
            {% endfor %}
        </body>
        </html>
        ''')
        with open(f"{filename}.html", "w") as f:
            f.write(template.render(report=self.report))

    def generate_report(self, format='html'):
        filename = f"reports/report_{self.domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        security_score = self.generate_security_score()
        self.report["security_analysis"]["score"] = security_score
        self.report["security_analysis"]["rating"] = (
            "A" if security_score >= 80 else
            "B" if security_score >= 60 else
            "C" if security_score >= 40 else
            "D" if security_score >= 20 else
            "F"
        )

        if format == 'console':
            print(json.dumps(self.report, indent=2))
        elif format == 'json':
            with open(f"{filename}.json", 'w') as f:
                json.dump(self.report, f, indent=2)
        else:
            self._generate_html_report(filename)

    def run(self, output_format='html'):
        print(f"[*] Iniciando análisis para {self.domain}")
        self.run_dns_scan()
        self.run_whois_lookup()
        
        dorks = {
            "config_files": f"site:{self.domain} filetype:env OR filetype:config OR filetype:ini",
            "exposed_dirs": f"site:{self.domain} intitle:'index of' OR 'directory listing'",
            "sensitive_files": f"site:{self.domain} ext:sql OR ext:bak OR ext:old OR ext:log"
        }
        
        for name, query in dorks.items():
            print(f"[*] Ejecutando dork: {query}")
            self.google_dork(query, name)
        
        self.generate_report(output_format)
        print("[+] Análisis completado!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ReconBot - Auditoría de Seguridad')
    parser.add_argument('domain', help='Dominio a analizar')
    parser.add_argument('--format', choices=['json', 'html', 'console'], default='html',
                      help='Formato del reporte (default: html)')
    
    args = parser.parse_args()
    bot = ReconBot(args.domain)
    bot.run(args.format)
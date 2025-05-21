from reconbot.dns_scanner import run_dns_scan
from reconbot.whois_lookup import run_whois_lookup
from reconbot.dorking import run_dorking
from reconbot.score import generate_security_score
from reconbot.report_generator import generate_report
from datetime import datetime

class ReconBotRunner:
    def __init__(self, domain):
        self.domain = domain
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

    def run(self, output_format='html'):
        print(f"[*] Iniciando análisis para {self.domain}")
        run_dns_scan(self.domain, self.report)
        run_whois_lookup(self.domain, self.report)
        run_dorking(self.domain, self.report)
        score, rating = generate_security_score(self.report)
        self.report["security_analysis"]["score"] = score
        self.report["security_analysis"]["rating"] = rating
        generate_report(self.domain, self.report, output_format)
        print("[+] Análisis completado!")

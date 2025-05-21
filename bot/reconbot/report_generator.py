import json
from datetime import datetime
from jinja2 import Template

def generate_report(domain, report, fmt='html'):
    filename = f"reports/report_{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    if fmt == 'console':
        print(json.dumps(report, indent=2))
    elif fmt == 'json':
        with open(f"{filename}.json", 'w') as f:
            json.dump(report, f, indent=2)
    else:
        with open(f"{filename}.html", "w") as f:
            f.write(Template(_html_template).render(report=report))

_html_template = '''<!DOCTYPE html>
<html>
<head>
    <title>Reporte - {{ report.metadata.domain }}</title>
    <style>
        body { font-family: Arial; margin: 2em; }
        .section { background: #f8f9fa; padding: 1em; margin-bottom: 1em; border-radius: 5px; }
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

    <div class="section"><h2>DNS</h2><pre>{{ report.dns | tojson(indent=2) }}</pre></div>
    <div class="section"><h2>WHOIS</h2><pre>{{ report.whois | tojson(indent=2) }}</pre></div>

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
</html>'''

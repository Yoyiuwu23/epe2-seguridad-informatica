# bot/reconbot/semantic_analyzer.py
import requests

def run_semantic_analysis(domain, report):
    try:
        text = f"El dominio {domain} fue analizado pasivamente."
        response = requests.post("http://api:8000/analizar/", json={"texto": text}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            report["security_analysis"]["semantic"] = data
        else:
            report["security_analysis"]["semantic"] = {
                "error": f"Error {response.status_code}: {response.text}"
            }
    except Exception as e:
        report["security_analysis"]["semantic"] = {"error": str(e)}

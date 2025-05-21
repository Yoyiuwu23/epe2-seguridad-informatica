import whois
from datetime import datetime

def run_whois_lookup(domain, report):
    try:
        w = whois.whois(domain)
        report["whois"] = {
            "registrar": w.registrar,
            "creation_date": str(w.creation_date),
            "expiration_date": str(w.expiration_date),
            "name_servers": list(w.name_servers) if w.name_servers else [],
            "status": w.status,
            "emails": w.emails if isinstance(w.emails, list) else [w.emails] if w.emails else []
        }

        domain_age = (datetime.now() - w.creation_date).days if w.creation_date else 0
        report["security_analysis"]["whois"] = {
            "domain_age_days": domain_age,
            "is_expired": w.expiration_date < datetime.now() if w.expiration_date else False,
            "privacy_protection": "PRIVACY" in str(w.status).upper()
        }
    except Exception as e:
        report["whois"] = {"error": str(e)}
        report["security_analysis"]["whois"] = {"error": "No se pudo obtener información WHOIS"}

def generate_security_score(report):
    score = 100

    a_records = report["dns"].get("A", [])
    if isinstance(a_records, str) and a_records.startswith("Error:"):
        score -= 40
    elif isinstance(a_records, list) and not a_records:
        score -= 20

    if not report["security_analysis"]["dns"].get("has_spf", False):
        score -= 15
    if not report["security_analysis"]["dns"].get("has_dmarc", False):
        score -= 15
    if any(d.get("results") for d in report["dorks"].values()):
        score -= 30

    if report["security_analysis"]["dns"].get("has_secure_ns", False):
        score += 10
    if report["security_analysis"]["whois"].get("privacy_protection", False):
        score += 5

    score = max(0, min(100, score))
    rating = (
        "A" if score >= 80 else
        "B" if score >= 60 else
        "C" if score >= 40 else
        "D" if score >= 20 else
        "F"
    )

    return score, rating

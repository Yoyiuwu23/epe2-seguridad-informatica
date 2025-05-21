import dns.resolver

def run_dns_scan(domain, report):
    records = ['A', 'MX', 'NS', 'SOA', 'TXT']
    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    resolver.lifetime = 5
    
    for record in records:
        try:
            answers = resolver.resolve(domain, record)
            report["dns"][record] = [str(r) for r in answers]
        except Exception as e:
            report["dns"][record] = f"Error: {str(e)}"

    txt_records = report["dns"].get("TXT", [])
    ns_records = report["dns"].get("NS", [])

    report["security_analysis"]["dns"] = {
        "has_dmarc": any("v=DMARC1" in str(r) for r in txt_records),
        "has_spf": any("v=spf1" in str(r).lower() for r in txt_records),
        "has_secure_ns": any("cloudflare" in ns.lower() or "awsdns" in ns.lower() 
                             for ns in ns_records)
    }

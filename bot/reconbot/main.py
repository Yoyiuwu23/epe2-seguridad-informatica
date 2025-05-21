import argparse
from reconbot.runner import ReconBotRunner

def main():
    parser = argparse.ArgumentParser(description="ReconBot - Auditoría pasiva de dominios.")
    parser.add_argument("domain", help="Dominio a auditar")
    parser.add_argument("--format", choices=["html", "json"], default="html", help="Formato del reporte")
    args = parser.parse_args()

    runner = ReconBotRunner(domain=args.domain, report_format=args.format)
    runner.run()

if __name__ == "__main__":
    main()

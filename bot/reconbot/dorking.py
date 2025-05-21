import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from reconbot.utils import analyze_with_deepseek

def google_dork(query):
    try:
        url = f"https://www.google.com/search?q={quote_plus(query)}"
        headers = {
            'User-Agent': 'Mozilla/5.0'
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

        return results[:5]
    except Exception as e:
        return {"error": str(e)}

def run_dorking(domain, report):
    dorks = {
        "config_files": f"site:{domain} filetype:env OR filetype:config OR filetype:ini",
        "exposed_dirs": f"site:{domain} intitle:'index of' OR 'directory listing'",
        "sensitive_files": f"site:{domain} ext:sql OR ext:bak OR ext:old OR ext:log"
    }

    for name, query in dorks.items():
        print(f"[*] Ejecutando dork: {query}")
        results = google_dork(query)
        report["dorks"][name] = {
            "query": query,
            "results": results if isinstance(results, list) else []
        }

        if isinstance(results, list) and results:
            text = " ".join([r['title'] + " " + r['snippet'] for r in results])
            analysis = analyze_with_deepseek(text)
            report["dorks"][name]["analysis"] = analysis

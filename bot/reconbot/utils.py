import requests

def analyze_with_deepseek(text):
    try:
        response = requests.post(
            "http://api:8000/analyze/",
            json={"text": text[:3000]},
            headers={'Content-Type': 'application/json'},
            timeout=15
        )
        return response.json() if response.status_code == 200 else {"error": f"API status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

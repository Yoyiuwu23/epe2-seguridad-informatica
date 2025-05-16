@lru_cache(maxsize=128)
def analyze_security_content(self, text):
    headers = {
        "Authorization": f"Bearer {self.api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""Eres un experto en seguridad informática. Analiza este contenido y genera:
1. Clasificación: 'sensitive' o 'normal' (solo una palabra)
2. Análisis técnico: 2-3 líneas explicando riesgos
3. Recomendación: Acción sugerida

Contenido:
{text[:3000]}

Respuesta en formato JSON válido:
```json
{{
  "classification": "sensitive|normal",
  "analysis": "Explicación técnica aquí...",
  "recommendation": "Recomendación aquí..."
}}
```"""

    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": 300  # Permite respuestas más largas
    }

    try:
        response = requests.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            headers=headers,
            timeout=self.timeout
        )
        response.raise_for_status()
        
        # Extrae el JSON de la respuesta
        response_text = response.json()['choices'][0]['message']['content']
        start = response_text.find('```json') + 7  # Elimina el markdown
        end = response_text.rfind('```')
        json_str = response_text[start:end].strip()
        analysis_result = json.loads(json_str)  # Convierte a dict

        return {
            'classification': analysis_result['classification'],
            'analysis': analysis_result['analysis'],
            'recommendation': analysis_result['recommendation'],
            'model': 'deepseek-chat'
        }
    except Exception as e:
        return {
            'error': str(e),
            'classification': 'unknown',
            'analysis': 'Error al analizar',
            'recommendation': 'Verificar logs'
        }
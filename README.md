ReconBot - Auditor de Seguridad Automatizado 🔍🤖

Versión 1.0.2
Licencia: GPLv3
Repositorio: https://github.com/Yoyiuwu23/epe2-seguridad-informatica

Herramienta de auditoría pasiva que analiza sitios web y estima su nivel de seguridad en una escala de 0 a 100. Desarrollada con fines académicos como parte de una evaluación en Seguridad Informática.
📌 Descripción

ReconBot combina técnicas clásicas de recolección de información con análisis semántico asistido por IA. Su objetivo es entregar un informe claro y puntuado sobre la exposición de un dominio, usando fuentes públicas de información.
🔎 Funcionalidades clave
Funcionalidad	Descripción
🧬 Escaneo DNS	Obtención de registros A, MX, TXT, NS, SOA
📜 WHOIS	Consulta completa del dominio
🕵️‍♀️ Dorking	Búsqueda avanzada automatizada en Google
🤖 Análisis IA	Evaluación semántica vía modelo de lenguaje
📄 Informes	Generación en HTML (con gráfico), JSON, consola
🌟 Características
Módulo	Descripción
dns_scanner	Extrae registros públicos del DNS
whois_lookup	Consulta WHOIS utilizando socket nativo
dorking	Ejecuta queries de tipo Google Dork
semantic_analyzer	Procesa texto con una API propia local de IA
score	Calcula una puntuación del 0 al 100
report_generator	Crea informes HTML con gráfico visual circular
🛠️ Requisitos

    Python 3.8+

    Docker & Docker Compose

    Acceso a Internet

⚙️ Instalación Rápida

# Clonar el repositorio
git clone https://github.com/Yoyiuwu23/epe2-seguridad-informatica.git
cd epe2-seguridad-informatica

# Construir e iniciar contenedores
docker-compose up -d --build

# Ejecutar análisis
docker-compose run --rm bot python -m reconbot.main ejemplo.com --format html

📎 Formatos disponibles: html, json, console
🗂️ Estructura del Proyecto

📦 epe2-seguridad-informatica
├── 📂 api/                      # API de análisis con IA (Django)
│   ├── 📂 api/                  # Configuración del proyecto Django
│   │   ├── __init__.py
│   │   ├── settings.py ⚙️
│   │   ├── urls.py 🌐
│   │   └── wsgi.py 🚀
│   ├── 📂 app/
│   │   ├── __init__.py
│   │   ├── 📂 utils/
│   │   │   └── deepseek.py 🔍
│   │   └── views.py 🖥️
│   ├── Dockerfile 🐳
│   ├── manage.py ⚒️
│   └── requirements.txt 📦
├── 📂 bot/                      # Cliente principal de auditoría pasiva
│   ├── Dockerfile 🐳
│   ├── requirements.txt 📦
│   ├── 📂 reconbot/
│   │   ├── __init__.py
│   │   ├── main.py 🚀 Punto de entrada
│   │   ├── runner.py
│   │   ├── dns_scanner.py
│   │   ├── whois_lookup.py
│   │   ├── dorking.py
│   │   ├── semantic_analyzer.py 🤖
│   │   ├── score.py
│   │   ├── report_generator.py 📄
│   │   └── utils.py
├── 📂 reports/                  # Informes generados
│   └── report_pcfactory.cl_20250521_212836.html
├── docker-compose.yml 🐙
├── LICENSE 📜
└── README.md 📖

🧪 Estado del Proyecto

    Versión 1.0.2 — Modularización completa

✅ Se completó la separación de responsabilidades del código en módulos.
✅ El informe HTML ahora incluye gráfico circular dinámico para representar la puntuación.
⚠️ Algunos módulos requieren validación con pruebas automáticas.
Próximos pasos

    🔬 Añadir pruebas unitarias

    📚 Documentar cada módulo

    🧩 Mejorar validación de entradas y excepciones

    🧠 Integración futura con IA más avanzada

📜 Licencia

Este proyecto está licenciado bajo la GPL v3.
Desarrollado por Yoyiuwu23 — 2025.
Puedes redistribuirlo y/o modificarlo bajo los términos de la GNU General Public License.

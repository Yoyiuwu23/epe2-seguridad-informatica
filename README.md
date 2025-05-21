# ReconBot - Auditor de Seguridad Automatizado 🔍🤖

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?logo=gnu)
![GitHub last commit](https://img.shields.io/github/last-commit/Yoyiuwu23/epe2-seguridad-informatica?logo=github)

Herramienta de auditoría pasiva que analiza sitios web y estima su nivel de seguridad en una escala de 0 a 100.

Repositorio: https://github.com/Yoyiuwu23/epe2-seguridad-informatica

---

## 📌 Descripción

ReconBot es un bot de auditoría pasiva que combina técnicas clásicas de recolección de información con análisis semántico asistido por IA.

🚀 Perfecto para fines académicos - Desarrollado como parte de una evaluación en seguridad informática.

---

## 🔎 Funcionalidades clave:

- Escaneo DNS completo  
- Consultas WHOIS  
- Dorking automatizado  
- Análisis con IA  
- Sistema de puntuación inteligente  

---

## 🌟 Características

| Módulo      | Descripción                        |
|-------------|----------------------------------|
| Escaneo DNS | Registros A, MX, TXT, NS, SOA    |
| WHOIS       | Información detallada del dominio |
| Dorking     | Búsquedas automatizadas en Google |
| Análisis IA | Evaluación semántica de vulnerabilidades |
| Informes    | Generación en HTML, JSON y consola |

---

## 🛠️ Requisitos

- Python 3.8+  
- Docker y Docker Compose  
- Conexión a Internet  

---

## 🚀 Instalación Rápida

1. Clonar repositorio
2. 
git clone https://github.com/Yoyiuwu23/epe2-seguridad-informatica.git
cd epe2-seguridad-informatica

    Iniciar contenedores

docker-compose up -d --build

    Ejecutar análisis

docker-compose run --rm bot python -m reconbot.main ejemplo.com --format html

Formatos disponibles: html, json, console
🗂️ Estructura del Proyecto

📦 epe2-seguridad-informatica
├── 📂 api/ # API de análisis con IA
│ ├── 📂 api/ # Configuración Django
│ │ ├── init.py
│ │ ├── settings.py ⚙️ Configuración
│ │ ├── urls.py 🌐 Rutas principales
│ │ └── wsgi.py 🚀 WSGI config
│ ├── 📂 app/ # Aplicación principal
│ │ ├── init.py
│ │ ├── 📂 utils/
│ │ │ └── deepseek.py 🔍 Integración con DeepSeek
│ │ └── views.py 🖥️ Vistas API
│ ├── Dockerfile 🐳 Config contenedor API
│ ├── manage.py ⚒️ CLI Django
│ └── requirements.txt 📦 Dependencias Python
├── 📂 bot/ # Cliente de auditoría
│ ├── Dockerfile 🐳 Config contenedor Bot
│ ├── reconbot/ 🤖 Código modularizado principal
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── runner.py
│ │ ├── dns_scanner.py
│ │ ├── whois_lookup.py
│ │ ├── dorking.py
│ │ ├── score.py
│ │ ├── report_generator.py
│ │ └── utils.py
│ ├── requirements.txt 📦 Dependencias Python
│ ├── report_ipchile.cl_20250516.html
│ ├── report_pcfactory.cl_20250516.html
│ └── reports/ 📊 Informes generados
├── docker-compose.yml 🐙 Orquestación contenedores
├── LICENSE 📜 Licencia GPLv3
├── README.md 📖 Documentación

📜 Licencia

Este proyecto está bajo Licencia GPLv3.

Copyright (C) 2025 Yoyiuwu23

Este programa es software libre: puedes redistribuirlo y/o modificar bajo los términos de la GNU General Public License.
📌 Versión 1.0.1

Esta versión representa un avance importante en la organización del código del proyecto ReconBot, donde el archivo monolítico reconbot.py ha sido modularizado para mejorar la mantenibilidad, legibilidad y escalabilidad del código.
Cambios principales en la versión 1.0.1:

    Se dividió reconbot.py en varios módulos dentro de la carpeta reconbot/ para separar responsabilidades:

        main.py (punto de entrada)

        runner.py

        dns_scanner.py

        whois_lookup.py

        dorking.py

        score.py

        report_generator.py

        utils.py

    Se adaptaron las importaciones y la estructura del proyecto para soportar esta modularización.

Estado actual:

    Importante: Esta versión NO ES FUNCIONAL aún. La modularización está en progreso y algunos componentes pueden no estar completamente integrados o probados. Se recomienda no usar esta versión en entornos de producción.

Próximos pasos:

    Completar la integración entre módulos.

    Añadir pruebas unitarias para asegurar la funcionalidad.

    Documentar cada módulo individualmente.

    Corregir y validar el flujo completo del bot.

📧 Contacto

Proyecto académico desarrollado por Yoyiuwu23 para la asignatura de Seguridad Informática.

# ReconBot - Auditor de Seguridad Automatizado 🔍🤖

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python) 
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker) 
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg) 
![Status](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)
![GitHub last commit](https://img.shields.io/github/last-commit/Yoyiuwu23/epe2-seguridad-informatica)

Herramienta de auditoría pasiva que analiza sitios web y estima su nivel de seguridad en una escala de 0 a 100.

**Repositorio**: [https://github.com/Yoyiuwu23/epe2-seguridad-informatica](https://github.com/Yoyiuwu23/epe2-seguridad-informatica)

## 📌 Descripción

ReconBot es un bot de auditoría pasiva que combina técnicas clásicas de recolección de información con análisis semántico asistido por IA. 

🚀 **Perfecto para fines académicos** - Desarrollado como parte de una evaluación en seguridad informática.

🔎 **Funcionalidades clave**:
- Escaneo DNS completo
- Consultas WHOIS
- Dorking automatizado
- Análisis con IA
- Sistema de puntuación inteligente

## 🌟 Características

| Módulo           | Descripción                                  |
|------------------|--------------------------------------------|
| **Escaneo DNS**  | Registros A, MX, TXT, NS, SOA              |
| **WHOIS**        | Información detallada del dominio          |
| **Dorking**      | Búsquedas automatizadas en Google          |
| **Análisis IA**  | Evaluación semántica de vulnerabilidades   |
| **Informes**     | Generación en HTML, JSON y consola         |

## 🛠️ Requisitos

- Python 3.8+
- Docker y Docker Compose
- Conexión a Internet

## 🚀 Instalación Rápida

# 1. Clonar repositorio
git clone https://github.com/Yoyiuwu23/epe2-seguridad-informatica.git
cd epe2-seguridad-informatica

# 2. Iniciar contenedores
docker-compose up -d --build

# 3. Ejecutar análisis
docker-compose run --rm bot python reconbot.py ejemplo.com --format html

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
│
├── 📂 bot/ # Cliente de auditoría
│ ├── Dockerfile 🐳 Config contenedor Bot
│ ├── reconbot.py 🤖 Lógica principal
│ └── requirements.txt 📦 Dependencias Python
│
├── docker-compose.yml 🐙 Orquestación contenedores
├── LICENSE 📜 Licencia GPLv3
├── README.md 📖 Documentación
└── 📂 reports/ 📊 Informes generados

📜 Licencia

Este proyecto está bajo Licencia GPLv3.

Copyright (C) 2025 Yoyiuwu23

Este programa es software libre: puedes redistribuirlo y/o modificar
bajo los términos de la GNU General Public License.

📧 Contacto

Proyecto académico desarrollado por Yoyiuwu23 para la asignatura de Seguridad Informática.

GitHub

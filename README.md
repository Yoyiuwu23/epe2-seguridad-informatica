ReconBot - Auditor de Seguridad Automatizado
============================================

Autor: Yoyiuwu23  
Versión: 1.0  
Licencia: GNU General Public License v3.0  
Repositorio: https://github.com/Yoyiuwu23/epe2-seguridad-informatica

Descripción
-----------

ReconBot es un bot de auditoría pasiva que analiza sitios web públicos y estima cuán seguros son en una escala de 0 a 100. Está orientado a fines académicos, como parte de una evaluación en seguridad informática. Esta es la primera versión funcional del proyecto.

El bot combina técnicas clásicas de recolección de información (reconocimiento pasivo) con una capa de análisis semántico asistido por IA. Realiza búsquedas dorking en Google, consultas DNS, obtención de datos WHOIS y evalúa configuraciones de seguridad comunes. Luego, calcula una puntuación de seguridad y genera un informe en varios formatos.

Características
---------------

- Escaneo DNS (registros A, MX, TXT, NS, SOA)
- Consulta WHOIS para dominios
- Dorking automatizado con Google
- Análisis semántico de resultados mediante API externa de IA
- Sistema de puntaje de seguridad del 0 al 100
- Generación de informes en HTML, JSON o consola
- Contenerizado con Docker y Docker Compose

Requisitos
----------

- Python 3.8 o superior
- Docker y Docker Compose
- Acceso a Internet (para resolver dominios y enviar peticiones HTTP)

Instalación y uso rápido
------------------------

1. Clona este repositorio:

   git clone https://github.com/Yoyiuwu23/epe2-seguridad-informatica.git  
   cd epe2-seguridad-informatica

2. Construye los contenedores e inicia los servicios en segundo plano:

   docker-compose up -d --build

3. Ejecuta el bot:

   docker-compose run --rm bot python reconbot.py ejemplo.com --format html

   Puedes cambiar el formato por:  
   - html  
   - json  
   - console

4. Control de servicios individuales:

   docker-compose start bot        # Inicia solo el bot  
   docker-compose stop api         # Detiene solo la API

Estructura del Proyecto
------------------------

- reconbot.py → Lógica principal del bot
- Dockerfile → Imagen del contenedor del bot
- docker-compose.yml → Orquestación de contenedores
- api/ → Carpeta para el backend de análisis semántico con IA
- reports/ → Carpeta donde se almacenan los informes generados

Licencia
--------

Este proyecto se distribuye bajo la Licencia Pública General GNU v3.0.  
Puedes ver el texto completo de la licencia en el archivo LICENSE.txt o en:  
https://www.gnu.org/licenses/gpl-3.0.txt

Contacto
--------

Proyecto estudiantil creado por Yoyiuwu23 como parte de una evaluación de la asignatura Seguridad Informática.

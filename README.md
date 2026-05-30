# CyberSec Tools Ecosystem | SecOps Automation

Colección de utilidades desarrolladas en Python para la automatización de auditorías perimetrales, análisis pasivo de red y detección de intrusiones mediante análisis sintáctico de registros.

## 🛠️ Módulos Incluidos

### 1. Log Intrusion Parser (`/log_parser`)
* **Descripción:** Analizador estático de registros de servidores web (Nginx/Apache).
* **Lógica:** Implementa expresiones regulares (RegEx) inmutables para interceptar firmas de ataques alineadas al OWASP Top 10 (SQLi, XSS, Path Traversal).

### 2. Port Sanitizer (`/network_scanners`)
* **Descripción:** Escáner pasivo de puertos TCP/IP enfocado en OpSec.
* **Lógica:** Analiza la exposición de servicios y valida la existencia de cabeceras de seguridad (CSP, HSTS) mitigando ataques de reconocimiento masivo.

## 🛡️ Parámetros de Seguridad Aplicados
Todo el código fuente ha sido diseñado bajo principios de desarrollo seguro para prevenir vulnerabilidades de inyección lógica o fugas de información sensible (Anti-OSINT).
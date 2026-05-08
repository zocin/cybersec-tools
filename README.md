# 🔐 Cybersec Tools

Herramientas de ciberseguridad desarrolladas en Python para análisis y auditoría de seguridad.

**Desarrollado por:** Andrés Felipe Cuervo | Estudiante de Ingeniería en Seguridad de la Información

---

## 🛠️ Herramientas

### 1. Scanner de Puertos (`scanner.py`)
Escanea puertos de un host objetivo e identifica cuáles están abiertos o cerrados.
- Detección de puertos comunes (21, 22, 23, 25, 53, 80, 443, 3306, 8080, 8443)
- Reporte con fecha y hora
- Configurable para cualquier host

### 2. Verificador de Contraseñas (`password_checker.py`)
Analiza la fortaleza de contraseñas e identifica vulnerabilidades.
- Puntuación de 0 a 7
- Detecta contraseñas comunes
- Recomendaciones específicas de mejora
- Niveles: Muy débil / Débil / Media / Fuerte

### 3. Verificador de Seguridad Web (`web_security_checker.py`)
Audita cabeceras de seguridad HTTP de cualquier sitio web.
- Verificación de HTTPS
- Content-Security-Policy
- X-Frame-Options (protección clickjacking)
- X-Content-Type-Options
- HSTS (Strict-Transport-Security)
- Puntuación porcentual de seguridad

### 4. Detector de Phishing (`phishing_detector.py`)
Analiza URLs y detecta indicadores de phishing.
- Detección de dominios sospechosos
- Verificación de acortadores de URL
- Análisis de palabras clave maliciosas
- Detección de IPs en lugar de dominios
- Puntuación de riesgo con niveles

### 5. IP Lookup Tool (`ip_lookup.py`)
Obtiene información detallada sobre cualquier dirección IP.
- Geolocalización (país, ciudad, región)
- Información del ISP y organización
- Detección de proxies y hosting
- Resolución inversa de DNS

### 6. File Integrity Checker (`file_integrity.py`)
Monitorea la integridad de archivos mediante hashing SHA-256.
- Creación de baseline de archivos
- Detección de archivos modificados
- Detección de archivos eliminados o nuevos
- Reporte detallado de cambios

### 7. Two Factor Authentication (`two_factor_auth.py`)
Sistema de autenticación de dos factores con OTP.
- Generación de OTP de 6 dígitos
- Expiración configurable (30 segundos)
- Verificación con hashing de contraseña
- Simulación completa del flujo 2FA

---

## 💼 Servicios disponibles

¿Tu empresa necesita una auditoría básica de seguridad? Ofrezco:

- ✅ Análisis de seguridad web de tu sitio
- ✅ Evaluación de políticas de contraseñas
- ✅ Detección de URLs de phishing
- ✅ Monitoreo de integridad de archivos
- ✅ Reporte detallado con recomendaciones
- ✅ Precio accesible para pequeñas empresas

📧 Contacto: Nyx_polaris@outlook.es
🌐 Portafolio: https://zocin.github.io

---

## 🎓 Certificaciones

- Google Cybersecurity Professional Certificate
- Cisco Introduction to Cybersecurity
- Auditor Interno ISO/IEC 27001:2013
- INCIBE - Ciberseguridad para microempresas
- Fundamentos de Ciberseguridad - OIT

---

## ⚙️ Requisitos

Python 3.x

## 🚀 Uso

```bash
python scanner.py
python password_checker.py
python web_security_checker.py
python phishing_detector.py
python ip_lookup.py
python file_integrity.py
python two_factor_auth.py
```
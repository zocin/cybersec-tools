# 🔐 Cybersec Tools

Herramientas de ciberseguridad desarrolladas en Python para análisis y auditoría básica de seguridad en pequeñas y medianas empresas.

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

---

## 💼 Servicios disponibles

¿Tu empresa necesita una auditoría básica de seguridad? Ofrezco:

- ✅ Análisis de seguridad web de tu sitio
- ✅ Evaluación de políticas de contraseñas
- ✅ Reporte detallado con recomendaciones
- ✅ Precio accesible para pequeñas empresas

📧 Contacto: scheol534@gmail.com

---

## 🎓 Certificaciones

- Google Cybersecurity Professional Certificate
- Cisco Introduction to Cybersecurity
- Auditor Interno ISO/IEC 27001:2013
- INCIBE - Ciberseguridad para microempresas
- Fundamentos de Ciberseguridad - OIT

---

## ⚙️ Requisitos

## 🚀 Uso

```bash
python scanner.py
python password_checker.py
python web_security_checker.py
```
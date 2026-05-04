import re
import datetime

# URLs y patrones sospechosos conocidos
PALABRAS_SOSPECHOSAS = [
    'login', 'verify', 'account', 'secure', 'update', 'confirm',
    'banking', 'paypal', 'amazon', 'google', 'microsoft', 'apple',
    'password', 'credential', 'signin', 'wallet', 'free', 'winner',
    'click', 'urgent', 'suspended', 'limited', 'verify'
]

DOMINIOS_SOSPECHOSOS = [
    '.xyz', '.tk', '.ml', '.ga', '.cf', '.gq', '.top', '.club'
]

ACORTADORES = [
    'bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly',
    'short.link', 'rebrand.ly', 'is.gd'
]

def analizar_url(url):
    print(f"\n{'='*55}")
    print(f"  DETECTOR DE PHISHING")
    print(f"  Proyect— Ciberseguridad")
    print(f"  Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")
    print(f"  URL analizada: {url}\n")

    riesgo = 0
    alertas = []
    positivos = []

    # 1. Verificar HTTPS
    if url.startswith("https://"):
        positivos.append("Usa HTTPS")
    else:
        alertas.append("No usa HTTPS — conexión insegura")
        riesgo += 2

    # 2. Verificar longitud
    if len(url) > 75:
        alertas.append(f"URL muy larga ({len(url)} caracteres) — técnica común de ofuscación")
        riesgo += 1

    # 3. Verificar IP en lugar de dominio
    if re.search(r'http[s]?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
        alertas.append("Usa dirección IP en lugar de dominio — muy sospechoso")
        riesgo += 3

    # 4. Verificar palabras sospechosas
    url_lower = url.lower()
    palabras_encontradas = [p for p in PALABRAS_SOSPECHOSAS if p in url_lower]
    if palabras_encontradas:
        alertas.append(f"Palabras sospechosas detectadas: {', '.join(palabras_encontradas)}")
        riesgo += len(palabras_encontradas)

    # 5. Verificar dominios sospechosos
    for dominio in DOMINIOS_SOSPECHOSOS:
        if dominio in url_lower:
            alertas.append(f"Dominio de alto riesgo detectado: {dominio}")
            riesgo += 2

    # 6. Verificar acortadores
    for acortador in ACORTADORES:
        if acortador in url_lower:
            alertas.append(f"URL acortada con {acortador} — destino oculto")
            riesgo += 2

    # 7. Verificar múltiples subdominios
    try:
        dominio_parte = url.split("//")[-1].split("/")[0]
        subdominios = dominio_parte.count(".")
        if subdominios > 2:
            alertas.append(f"Múltiples subdominios ({subdominios}) — técnica de engaño")
            riesgo += 2
    except:
        pass

    # 8. Verificar caracteres especiales sospechosos
    if '@' in url:
        alertas.append("Símbolo @ en URL — puede redirigir a sitio diferente")
        riesgo += 3

    if '//' in url.replace("https://", "").replace("http://", ""):
        alertas.append("Doble barra sospechosa en URL")
        riesgo += 1

    # Resultado
    print("  ALERTAS DETECTADAS:")
    if alertas:
        for a in alertas:
            print(f"    ⚠️  {a}")
    else:
        print("    ✅ Sin alertas detectadas")

    if positivos:
        print("\n  ASPECTOS POSITIVOS:")
        for p in positivos:
            print(f"    ✅ {p}")

    # Nivel de riesgo
    if riesgo == 0:
        nivel = "SEGURA ✅"
    elif riesgo <= 2:
        nivel = "BAJA SOSPECHA 🟡"
    elif riesgo <= 5:
        nivel = "SOSPECHOSA 🟠"
    else:
        nivel = "PHISHING PROBABLE 🔴"

    print(f"\n{'='*55}")
    print(f"  Puntuación de riesgo: {riesgo}")
    print(f"  Nivel: {nivel}")
    print(f"{'='*55}\n")

# Pruebas
analizar_url("https://google.com")
analizar_url("http://192.168.1.1/login/verify/account")
analizar_url("https://secure-paypal-verify.xyz/login/confirm/account")
analizar_url("http://bit.ly/win-free-iphone")
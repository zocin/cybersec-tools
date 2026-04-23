import urllib.request
import urllib.error
import datetime
import ssl

def verificar_seguridad_web(url):
    print(f"\n{'='*55}")
    print(f"  VERIFICADOR DE SEGURIDAD WEB")
    print(f"  Andrés Felipe Cuervo - Ciberseguridad")
    print(f"  Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")
    
    if not url.startswith("http"):
        url = "https://" + url

    print(f"  Analizando: {url}\n")
    
    puntuacion = 0
    total = 6
    resultados = []

    # 1. Verificar HTTPS
    try:
        if url.startswith("https://"):
            resultados.append(("✅", "HTTPS activo", "El sitio usa conexión cifrada"))
            puntuacion += 1
        else:
            resultados.append(("❌", "Sin HTTPS", "El sitio NO usa conexión cifrada"))
    except:
        resultados.append(("❌", "Sin HTTPS", "No se pudo verificar"))

    # 2. Intentar conexión
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(url, headers={'User-Agent': 'SecurityChecker/1.0'})
        response = urllib.request.urlopen(req, timeout=10, context=ctx)
        headers = dict(response.headers)
        
        # 3. Content-Security-Policy
        if 'Content-Security-Policy' in headers:
            resultados.append(("✅", "Content-Security-Policy", "Protección contra inyección de código"))
            puntuacion += 1
        else:
            resultados.append(("❌", "Sin Content-Security-Policy", "Vulnerable a inyección de código"))

        # 4. X-Frame-Options
        if 'X-Frame-Options' in headers:
            resultados.append(("✅", "X-Frame-Options", "Protección contra clickjacking"))
            puntuacion += 1
        else:
            resultados.append(("❌", "Sin X-Frame-Options", "Vulnerable a clickjacking"))

        # 5. X-Content-Type-Options
        if 'X-Content-Type-Options' in headers:
            resultados.append(("✅", "X-Content-Type-Options", "Protección contra MIME sniffing"))
            puntuacion += 1
        else:
            resultados.append(("❌", "Sin X-Content-Type-Options", "Vulnerable a MIME sniffing"))

        # 6. Strict-Transport-Security
        if 'Strict-Transport-Security' in headers:
            resultados.append(("✅", "HSTS activo", "Fuerza uso de HTTPS siempre"))
            puntuacion += 1
        else:
            resultados.append(("❌", "Sin HSTS", "No fuerza uso de HTTPS"))

    except urllib.error.URLError as e:
        resultados.append(("⚠️", "Error de conexión", str(e)))
    except Exception as e:
        resultados.append(("⚠️", "Error inesperado", str(e)))

    # Mostrar resultados
    for icono, titulo, descripcion in resultados:
        print(f"  {icono} {titulo}")
        print(f"     → {descripcion}\n")

    # Puntuación final
    porcentaje = int((puntuacion / total) * 100)
    
    if porcentaje <= 30:
        nivel = "MUY INSEGURO 🔴"
    elif porcentaje <= 60:
        nivel = "INSEGURO 🟠"
    elif porcentaje <= 80:
        nivel = "ACEPTABLE 🟡"
    else:
        nivel = "SEGURO 🟢"

    print(f"{'='*55}")
    print(f"  Puntuación: {puntuacion}/{total} ({porcentaje}%)")
    print(f"  Nivel de seguridad: {nivel}")
    print(f"{'='*55}\n")

# Pruebas con sitios reales
verificar_seguridad_web("https://google.com")
verificar_seguridad_web("https://example.com")
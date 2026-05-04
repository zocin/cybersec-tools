import urllib.request
import urllib.error
import json
import datetime
import socket

def lookup_ip(ip):
    print(f"\n{'='*55}")
    print(f"  IP ADDRESS LOOKUP TOOL")
    print(f"  proyecto 5 — Ciberseguridad")
    print(f"  Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*55}\n")
    print(f"  Analizando IP: {ip}\n")

    alertas = []

    # 1. Verificar si es IP privada
    partes = ip.split(".")
    if len(partes) == 4:
        primer = int(partes[0])
        segundo = int(partes[1])
        if primer == 10:
            print(f"  ℹ️  IP Privada (rango 10.x.x.x)")
            return
        elif primer == 172 and 16 <= segundo <= 31:
            print(f"  ℹ️  IP Privada (rango 172.16-31.x.x)")
            return
        elif primer == 192 and segundo == 168:
            print(f"  ℹ️  IP Privada (rango 192.168.x.x)")
            return
        elif primer == 127:
            print(f"  ℹ️  IP Localhost (127.x.x.x)")
            return

    # 2. Consultar API pública
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,isp,org,as,proxy,hosting,query"
        req = urllib.request.Request(url, headers={'User-Agent': 'SecurityTool/1.0'})
        response = urllib.request.urlopen(req, timeout=10)
        data = json.loads(response.read().decode())

        if data.get('status') == 'success':
            print(f"  📍 UBICACIÓN:")
            print(f"     País:     {data.get('country', 'N/A')}")
            print(f"     Región:   {data.get('regionName', 'N/A')}")
            print(f"     Ciudad:   {data.get('city', 'N/A')}")
            print(f"\n  🌐 RED:")
            print(f"     ISP:      {data.get('isp', 'N/A')}")
            print(f"     Org:      {data.get('org', 'N/A')}")
            print(f"     AS:       {data.get('as', 'N/A')}")

            # Alertas de seguridad
            if data.get('proxy'):
                alertas.append("Proxy detectado — IP puede estar ocultando identidad")
            if data.get('hosting'):
                alertas.append("IP de hosting/datacenter — puede ser servidor malicioso")

        else:
            print(f"  ⚠️  No se pudo obtener información: {data.get('message', 'Error desconocido')}")

    except Exception as e:
        print(f"  ⚠️  Error consultando API: {e}")

    # 3. Resolución inversa DNS
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"\n  🔍 DNS INVERSO:")
        print(f"     Hostname: {hostname}")
    except:
        print(f"\n  🔍 DNS INVERSO: No disponible")

    # 4. Mostrar alertas
    if alertas:
        print(f"\n  ⚠️  ALERTAS DE SEGURIDAD:")
        for a in alertas:
            print(f"     🔴 {a}")
    else:
        print(f"\n  ✅ Sin alertas de seguridad detectadas")

    print(f"\n{'='*55}\n")

# Pruebas
lookup_ip("127.0.0.1")
lookup_ip("8.8.8.8")
lookup_ip("192.168.1.1")
lookup_ip("1.1.1.1")
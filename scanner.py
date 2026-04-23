import socket
import datetime

def escanear_puertos(host, puertos):
    print(f"\n{'='*50}")
    print(f"  ESCÁNER DE PUERTOS ")
    print(f"  Objetivo: {host}")
    print(f"  Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")
    
    puertos_abiertos = []
    
    for puerto in puertos:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            resultado = sock.connect_ex((host, puerto))
            if resultado == 0:
                print(f"  [ABIERTO] Puerto {puerto}")
                puertos_abiertos.append(puerto)
            else:
                print(f"  [cerrado] Puerto {puerto}")
            sock.close()
        except Exception as e:
            print(f"  [error] Puerto {puerto}: {e}")
    
    print(f"\n{'='*50}")
    print(f"  Puertos abiertos encontrados: {len(puertos_abiertos)}")
    print(f"{'='*50}\n")

# Puertos comunes a escanear
puertos_comunes = [21, 22, 23, 25, 53, 80, 443, 3306, 8080, 8443]

# Escanear localhost como prueba
escanear_puertos("127.0.0.1", puertos_comunes)
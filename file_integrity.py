import hashlib
import os
import json
import datetime

def calcular_hash(filepath, algoritmo='sha256'):
    h = hashlib.new(algoritmo)
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except:
        return None

def crear_baseline(directorio, archivo_baseline='baseline.json'):
    print("\n" + "="*55)
    print("  FILE INTEGRITY CHECKER")
    print("  Andres Felipe Cuervo - Ciberseguridad")
    print("  Fecha: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*55 + "\n")
    print("  Creando baseline de: " + directorio + "\n")

    baseline = {}
    archivos_procesados = 0

    for root, dirs, files in os.walk(directorio):
        for archivo in files:
            ruta = os.path.join(root, archivo)
            hash_val = calcular_hash(ruta)
            if hash_val:
                baseline[ruta] = {
                    'hash': hash_val,
                    'tamanio': os.path.getsize(ruta),
                    'fecha': datetime.datetime.now().isoformat()
                }
                print("  OK " + archivo + " -> " + hash_val[:16] + "...")
                archivos_procesados += 1

    with open(archivo_baseline, 'w') as f:
        json.dump(baseline, f, indent=2)

    print("\n  Baseline creado: " + str(archivos_procesados) + " archivos registrados")
    print("  Guardado en: " + archivo_baseline)
    print("="*55 + "\n")
    return baseline

def verificar_integridad(directorio, archivo_baseline='baseline.json'):
    print("\n" + "="*55)
    print("  VERIFICACION DE INTEGRIDAD")
    print("  Fecha: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*55 + "\n")

    if not os.path.exists(archivo_baseline):
        print("  ERROR: No existe baseline.")
        return

    with open(archivo_baseline, 'r') as f:
        baseline = json.load(f)

    modificados = []
    eliminados = []
    nuevos = []

    for ruta, info in baseline.items():
        if not os.path.exists(ruta):
            eliminados.append(ruta)
        else:
            hash_actual = calcular_hash(ruta)
            if hash_actual != info['hash']:
                modificados.append({
                    'archivo': ruta,
                    'hash_original': info['hash'][:16],
                    'hash_actual': hash_actual[:16]
                })

    for root, dirs, files in os.walk(directorio):
        for archivo in files:
            ruta = os.path.join(root, archivo)
            if ruta not in baseline and archivo != archivo_baseline:
                nuevos.append(ruta)

    total_alertas = len(modificados) + len(eliminados) + len(nuevos)

    if modificados:
        print("  ARCHIVOS MODIFICADOS (" + str(len(modificados)) + "):")
        for m in modificados:
            print("    ALERTA: " + os.path.basename(m['archivo']))
            print("    Original: " + m['hash_original'] + "...")
            print("    Actual:   " + m['hash_actual'] + "...")

    if eliminados:
        print("\n  ARCHIVOS ELIMINADOS (" + str(len(eliminados)) + "):")
        for e in eliminados:
            print("    ALERTA: " + os.path.basename(e))

    if nuevos:
        print("\n  ARCHIVOS NUEVOS (" + str(len(nuevos)) + "):")
        for n in nuevos:
            print("    NUEVO: " + os.path.basename(n))

    if total_alertas == 0:
        print("  OK: Integridad verificada - Sin cambios detectados")
    else:
        print("\n  Total de alertas: " + str(total_alertas))

    print("="*55 + "\n")

directorio_prueba = "."
crear_baseline(directorio_prueba)
verificar_integridad(directorio_prueba)
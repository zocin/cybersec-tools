import re
import datetime

def verificar_contrasena(password):
    print(f"\n{'='*50}")
    print(f"  VERIFICADOR DE CONTRASEÑAS")
    print(f"  Andrés Felipe Cuervo - Ciberseguridad")
    print(f"  Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")
    
    puntuacion = 0
    problemas = []
    recomendaciones = []

    # Longitud
    if len(password) < 8:
        problemas.append("Muy corta (menos de 8 caracteres)")
        recomendaciones.append("Usa mínimo 8 caracteres")
    elif len(password) >= 12:
        puntuacion += 2
    else:
        puntuacion += 1

    # Mayúsculas
    if re.search(r'[A-Z]', password):
        puntuacion += 1
    else:
        problemas.append("Sin letras mayúsculas")
        recomendaciones.append("Agrega al menos una mayúscula")

    # Minúsculas
    if re.search(r'[a-z]', password):
        puntuacion += 1
    else:
        problemas.append("Sin letras minúsculas")
        recomendaciones.append("Agrega al menos una minúscula")

    # Números
    if re.search(r'[0-9]', password):
        puntuacion += 1
    else:
        problemas.append("Sin números")
        recomendaciones.append("Agrega al menos un número")

    # Caracteres especiales
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        puntuacion += 2
    else:
        problemas.append("Sin caracteres especiales")
        recomendaciones.append("Agrega símbolos como !@#$%")

    # Contraseñas comunes
    comunes = ["123456", "password", "admin", "qwerty", "abc123", "contraseña"]
    if password.lower() in comunes:
        puntuacion = 0
        problemas.append("Contraseña extremadamente común")

    # Resultado
    if puntuacion <= 2:
        nivel = "MUY DÉBIL 🔴"
    elif puntuacion <= 3:
        nivel = "DÉBIL 🟠"
    elif puntuacion <= 5:
        nivel = "MEDIA 🟡"
    else:
        nivel = "FUERTE 🟢"

    print(f"  Contraseña analizada: {'*' * len(password)}")
    print(f"  Puntuación: {puntuacion}/7")
    print(f"  Nivel: {nivel}\n")

    if problemas:
        print("  Problemas encontrados:")
        for p in problemas:
            print(f"    ❌ {p}")
    
    if recomendaciones:
        print("\n  Recomendaciones:")
        for r in recomendaciones:
            print(f"    ✅ {r}")
    
    print(f"\n{'='*50}\n")

# Pruebas
verificar_contrasena("123456")
verificar_contrasena("MiEmpresa2024")
verificar_contrasena("S3gur!dad#2024")
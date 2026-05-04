import random
import time
import datetime
import hashlib

def generar_otp(longitud=6):
    return str(random.randint(10**(longitud-1), 10**longitud - 1))

def enviar_otp(usuario, otp):
    print("\n" + "="*55)
    print("  SISTEMA DE AUTENTICACION DE DOS FACTORES")
    print("  Andres Felipe Cuervo - Ciberseguridad")
    print("  Fecha: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*55 + "\n")
    print("  Usuario: " + usuario)
    print("  OTP generado: " + otp + " (simulado - en produccion se envia por SMS/email)")
    print("  Expira en: 30 segundos\n")

def verificar_otp(otp_ingresado, otp_real, tiempo_generacion, expiracion=30):
    tiempo_actual = time.time()
    tiempo_transcurrido = tiempo_actual - tiempo_generacion

    if tiempo_transcurrido > expiracion:
        return False, "OTP expirado"

    if otp_ingresado == otp_real:
        return True, "Autenticacion exitosa"
    else:
        return False, "OTP incorrecto"

def simular_login_2fa(usuario, password_correcta):
    print("\n" + "="*55)
    print("  SIMULACION DE LOGIN CON 2FA")
    print("="*55 + "\n")

    # Paso 1 - Verificar password
    print("  PASO 1: Verificacion de contrasena")
    password_hash = hashlib.sha256(password_correcta.encode()).hexdigest()
    print("  Hash de contrasena: " + password_hash[:20] + "...")
    print("  Contrasena correcta: OK\n")

    # Paso 2 - Generar OTP
    print("  PASO 2: Generacion de OTP")
    otp = generar_otp()
    tiempo_generacion = time.time()
    enviar_otp(usuario, otp)

    # Paso 3 - Verificar OTP
    print("  PASO 3: Verificacion de OTP")

    # Simulacion 1: OTP correcto
    print("  Intento 1 - OTP correcto:")
    exito, mensaje = verificar_otp(otp, otp, tiempo_generacion)
    if exito:
        print("  OK " + mensaje)
    else:
        print("  ERROR " + mensaje)

    # Simulacion 2: OTP incorrecto
    print("\n  Intento 2 - OTP incorrecto:")
    exito, mensaje = verificar_otp("000000", otp, tiempo_generacion)
    if exito:
        print("  OK " + mensaje)
    else:
        print("  ERROR " + mensaje)

    # Simulacion 3: OTP expirado
    print("\n  Intento 3 - OTP expirado (simulado):")
    tiempo_pasado = time.time() - 60
    exito, mensaje = verificar_otp(otp, otp, tiempo_pasado)
    if exito:
        print("  OK " + mensaje)
    else:
        print("  ERROR " + mensaje)

    print("\n" + "="*55)
    print("  RESUMEN DE SEGURIDAD 2FA:")
    print("  - Capa 1: Contrasena (algo que sabes)")
    print("  - Capa 2: OTP (algo que tienes)")
    print("  - Expiracion: 30 segundos")
    print("  - Longitud OTP: 6 digitos")
    print("  - Intentos maximos recomendados: 3")
    print("="*55 + "\n")

# Demo
simular_login_2fa("andres.cuervo", "MiContrasenaSegura2024!")
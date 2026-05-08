import hashlib
import os
import json
import datetime

ARCHIVO_USUARIOS = "usuarios.json"

def cargar_usuarios():
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, 'r') as f:
            return json.load(f)
    return {}

def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=2)

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(32).hex()
    hash_val = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return hash_val.hex(), salt

def registrar_usuario(username, password):
    usuarios = cargar_usuarios()
    
    if username in usuarios:
        return False, "Usuario ya existe"
    
    if len(password) < 8:
        return False, "Contrasena muy corta (minimo 8 caracteres)"
    
    hash_val, salt = hash_password(password)
    usuarios[username] = {
        'hash': hash_val,
        'salt': salt,
        'fecha_registro': datetime.datetime.now().isoformat(),
        'intentos_fallidos': 0
    }
    guardar_usuarios(usuarios)
    return True, "Usuario registrado exitosamente"

def iniciar_sesion(username, password):
    usuarios = cargar_usuarios()
    
    if username not in usuarios:
        return False, "Usuario no encontrado"
    
    usuario = usuarios[username]
    
    if usuario['intentos_fallidos'] >= 3:
        return False, "Cuenta bloqueada por multiples intentos fallidos"
    
    hash_val, _ = hash_password(password, usuario['salt'])
    
    if hash_val == usuario['hash']:
        usuario['intentos_fallidos'] = 0
        guardar_usuarios(usuarios)
        return True, "Login exitoso"
    else:
        usuario['intentos_fallidos'] += 1
        guardar_usuarios(usuarios)
        restantes = 3 - usuario['intentos_fallidos']
        return False, "Contrasena incorrecta. Intentos restantes: " + str(restantes)

def demo():
    print("\n" + "="*55)
    print("  LOGIN SYSTEM WITH HASHING")
    print("  Andres Felipe Cuervo - Ciberseguridad")
    print("  Fecha: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*55 + "\n")

    print("  REGISTRO DE USUARIOS:")
    
    exito, msg = registrar_usuario("andres", "MiPassword2024!")
    print("  Registrar 'andres': " + msg)
    
    exito, msg = registrar_usuario("admin", "Admin123!")
    print("  Registrar 'admin': " + msg)
    
    exito, msg = registrar_usuario("andres", "OtraPassword!")
    print("  Registrar 'andres' de nuevo: " + msg)

    print("\n  INTENTOS DE LOGIN:")
    
    exito, msg = iniciar_sesion("andres", "MiPassword2024!")
    print("  Login correcto: " + msg)
    
    exito, msg = iniciar_sesion("andres", "passwordincorrecta")
    print("  Login incorrecto: " + msg)
    
    exito, msg = iniciar_sesion("andres", "otraincorrecta")
    print("  Login incorrecto 2: " + msg)
    
    exito, msg = iniciar_sesion("andres", "otramas")
    print("  Login incorrecto 3: " + msg)
    
    exito, msg = iniciar_sesion("andres", "MiPassword2024!")
    print("  Intento despues de bloqueo: " + msg)

    print("\n  CONCEPTOS DE SEGURIDAD APLICADOS:")
    print("  - PBKDF2 con SHA-256 (100,000 iteraciones)")
    print("  - Salt unico por usuario (protege contra rainbow tables)")
    print("  - Bloqueo tras 3 intentos fallidos")
    print("  - Validacion de longitud de contrasena")
    print("  - Nunca se almacena la contrasena en texto plano")
    print("\n" + "="*55 + "\n")

demo()
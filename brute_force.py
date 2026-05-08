import hashlib
import time
import datetime
import itertools
import string

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_simple(hash_objetivo, longitud_max=4):
    print("\n  ATAQUE 1: FUERZA BRUTA PURA")
    print("  Probando todas las combinaciones posibles...")
    
    caracteres = string.ascii_lowercase + string.digits
    intentos = 0
    inicio = time.time()

    for longitud in range(1, longitud_max + 1):
        for combo in itertools.product(caracteres, repeat=longitud):
            password = ''.join(combo)
            intentos += 1
            if hash_password(password) == hash_objetivo:
                tiempo = time.time() - inicio
                print("  ENCONTRADO: " + password)
                print("  Intentos: " + str(intentos))
                print("  Tiempo: " + str(round(tiempo, 3)) + " segundos")
                return password
    
    print("  No encontrado en " + str(intentos) + " intentos")
    return None

def ataque_diccionario(hash_objetivo):
    print("\n  ATAQUE 2: DICCIONARIO")
    print("  Probando contrasenas comunes...")
    
    diccionario = [
        "123456", "password", "admin", "qwerty", "abc123",
        "letmein", "monkey", "1234567", "dragon", "master",
        "welcome", "login", "pass", "test", "hello",
        "colombia", "bogota", "andres", "felipe", "seguridad"
    ]
    
    intentos = 0
    inicio = time.time()
    
    for palabra in diccionario:
        intentos += 1
        if hash_password(palabra) == hash_objetivo:
            tiempo = time.time() - inicio
            print("  ENCONTRADO: " + palabra)
            print("  Intentos: " + str(intentos))
            print("  Tiempo: " + str(round(tiempo, 4)) + " segundos")
            return palabra
    
    print("  No encontrado en diccionario (" + str(intentos) + " palabras)")
    return None

def demo():
    print("\n" + "="*55)
    print("  BRUTE FORCE SIMULATION")
    print("  Andres Felipe Cuervo - Ciberseguridad")
    print("  Fecha: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*55)
    
    print("\n  OBJETIVO EDUCATIVO:")
    print("  Demostrar por que las contrasenas debiles son peligrosas")
    print("  SOLO para uso educativo y en entornos controlados\n")

    # Password debil - facil de crackear
    password_debil = "abc"
    hash_debil = hash_password(password_debil)
    print("  TARGET 1: Contrasena debil")
    print("  Hash SHA-256: " + hash_debil[:20] + "...")
    brute_force_simple(hash_debil, longitud_max=3)

    # Password de diccionario
    password_dic = "colombia"
    hash_dic = hash_password(password_dic)
    print("\n  TARGET 2: Contrasena de diccionario")
    print("  Hash SHA-256: " + hash_dic[:20] + "...")
    ataque_diccionario(hash_dic)

    # Password fuerte - imposible de crackear
    password_fuerte = "X9#mK2$pL8@nQ4!"
    hash_fuerte = hash_password(password_fuerte)
    print("\n  TARGET 3: Contrasena fuerte")
    print("  Hash SHA-256: " + hash_fuerte[:20] + "...")
    print("\n  ATAQUE 1: FUERZA BRUTA PURA")
    print("  Esta contrasena tiene 16 caracteres con simbolos.")
    print("  Tiempo estimado para crackear: miles de anos.")
    print("  Simulacion omitida por razones obvias.")
    ataque_diccionario(hash_fuerte)

    print("\n" + "="*55)
    print("  CONCLUSIONES DE SEGURIDAD:")
    print("  - Contrasenas cortas: crackeables en segundos")
    print("  - Palabras del diccionario: crackeables en milisegundos")
    print("  - Contrasenas largas con simbolos: practicamente imposibles")
    print("  - Usar siempre: minimo 12 caracteres, mayusculas,")
    print("    minusculas, numeros y simbolos")
    print("  - Hashing moderno recomendado: bcrypt, Argon2, PBKDF2")
    print("="*55 + "\n")

demo()
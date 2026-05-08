import datetime

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)

def fuerza_bruta_cesar(texto_cifrado):
    print("\n  ATAQUE POR FUERZA BRUTA:")
    for i in range(1, 26):
        intento = descifrar_cesar(texto_cifrado, i)
        print(f"  Desplazamiento {i:2d}: {intento}")

def analizar_cesar(texto):
    print("\n" + "="*55)
    print("  CAESAR CIPHER ENCRYPTION TOOL")
    print("  Proyecto_Ciberseguridad")
    print("  Fecha: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*55 + "\n")

    desplazamiento = 13

    print("  TEXTO ORIGINAL:  " + texto)
    
    cifrado = cifrar_cesar(texto, desplazamiento)
    print("  TEXTO CIFRADO:   " + cifrado)
    print("  DESPLAZAMIENTO:  " + str(desplazamiento))

    descifrado = descifrar_cesar(cifrado, desplazamiento)
    print("  TEXTO DESCIFRADO:" + descifrado)

    print("\n  EXPLICACION:")
    print("  El cifrado Cesar desplaza cada letra N posiciones en el alfabeto.")
    print("  Ejemplo con desplazamiento 3: A->D, B->E, C->F")
    print("  Es uno de los cifrados mas antiguos, usado por Julio Cesar.")
    print("  HOY EN DIA ES INSEGURO - demostrable con fuerza bruta:\n")

    fuerza_bruta_cesar(cifrado)

    print("\n" + "="*55)
    print("  CONCLUSION DE SEGURIDAD:")
    print("  El cifrado Cesar tiene solo 25 combinaciones posibles.")
    print("  Un atacante puede probar todas en segundos.")
    print("  NUNCA usar para proteger informacion real.")
    print("  Algoritmos modernos recomendados: AES-256, RSA, ChaCha20")
    print("="*55 + "\n")

# Demo
analizar_cesar("Hola Mundo desde Colombia")
analizar_cesar("Ciberseguridad es las calabazas")

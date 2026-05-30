import re

def analyze_log_line(log_line):
    print(f"[*] Analizando evento: {log_line}")

    # Expresiones regulares para detectar patrones de inyección comunes (OWASP Top 10)
    sqli_pattern = re.compile(r"(UNION|SELECT|INSERT|DELETE|WHERE|OR\s+\d+=\d+)", re.IGNORECASE)
    xss_pattern = re.compile(r"(<script>|javascript:|onerror|onload)", re.IGNORECASE)

    # Evaluación heurística
    if sqli_pattern.search(log_line):
        return "[!] ALERTA CRÍTICA: Intento de Inyección SQL (SQLi) detectado y mitigado."
    elif xss_pattern.search(log_line):
        return "[!] ALERTA CRÍTICA: Intento de Cross-Site Scripting (XSS) detectado y mitigado."
    else:
        return "[+] Transmisión segura: Registro conforme a las políticas SecOps."

if __name__ == "__main__":
    # Simulación de un log malicioso interceptado
    log_payload = "GET /index.php?id=1' UNION SELECT NULL, username, password FROM users--"
    resultado = analyze_log_line(log_payload)
    print(resultado)
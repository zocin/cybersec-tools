def audit_target_ports(target_host):
    print(f"[*] Iniciando auditoría pasiva en el host objetivo: {target_host}")

    # Base de datos simulada de puertos encontrados y su estado
    infrastructure_status = {
        22: {"service": "SSH", "status": "Abierto", "alert": "Banner expone versión desactualizada."},
        80: {"service": "HTTP", "status": "Mitigado", "alert": "Protección activa: Encabezados CSP/HSTS validados."},
        445: {"service": "SMB", "status": "Crítico", "alert": "Protocolo heredado y vulnerable SMBv1 activo."}
    }

    for port, info in infrastructure_status.items():
        print(f"\n[-] Evaluando Puerto {port}/TCP ({info['service']}) -> Estado: {info['status']}")
        print(f"    [!] Reporte de Riesgo: {info['alert']}")

if __name__ == "__main__":
    audit_target_ports("10.0.0.15")
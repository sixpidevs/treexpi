# netspresso/utils/helpers.py

def validate_domain_name(domain_name):
    """Valida si un nombre de dominio es sintácticamente correcto."""
    # Esta es una validación básica. Puedes ampliarla según tus necesidades.
    if not domain_name or "." not in domain_name:
        return False
    return True

def format_dns_record(record):
    """Formatea un registro DNS para su visualización."""
    return f"Tipo: {record['type']}, Nombre: {record['name']}, Contenido: {record['content']}"

def log(message, level="info"):
    """Registra un mensaje en el log, con un nivel de severidad."""
    # Implementación básica. Puedes expandirla para integrar con un sistema de logging real.
    print(f"[{level.upper()}] {message}")

# Puedes agregar más funciones de utilidad según sea necesario.


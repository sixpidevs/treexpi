# api/cloudflare.py

import os
import requests
from decouple import config

# Obtener variables de configuración desde el archivo .env
CLOUDFLARE_API_KEY = config('CLOUDFLARE_API_KEY')
CLOUDFLARE_EMAIL = config('CLOUDFLARE_EMAIL')

# URL base de la API de Cloudflare
CLOUDFLARE_BASE_URL = "https://api.cloudflare.com/client/v4"

# Encabezados comunes para las solicitudes HTTP a la API de Cloudflare
HEADERS = {
    "X-Auth-Email": CLOUDFLARE_EMAIL,
    "X-Auth-Key": CLOUDFLARE_API_KEY,
    "Content-Type": "application/json"
}

def list_zones():
    """Listar todas las zonas disponibles en Cloudflare para la cuenta."""
    url = f"{CLOUDFLARE_BASE_URL}/zones"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  # Lanza una excepción para respuestas fallidas
    data = response.json()
    return data

def create_dns_record(zone_id, type, name, content):
    """Crear un registro DNS en una zona específica."""
    url = f"{CLOUDFLARE_BASE_URL}/zones/{zone_id}/dns_records"
    data = {
        "type": type,
        "name": name,
        "content": content
    }
    response = requests.post(url, headers=HEADERS, json=data)
    response.raise_for_status()
    return response.json()

def delete_dns_record(zone_id, record_id):
    """Eliminar un registro DNS de una zona específica."""
    url = f"{CLOUDFLARE_BASE_URL}/zones/{zone_id}/dns_records/{record_id}"
    response = requests.delete(url, headers=HEADERS)
    response.raise_for_status()
   

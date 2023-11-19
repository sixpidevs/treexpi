# Netspresso Cloudflare Module

## Descripción
El módulo Cloudflare de Netspresso es una herramienta diseñada para facilitar la interacción con la API de Cloudflare. Permite realizar operaciones como listar zonas, crear y eliminar registros DNS de manera programática, simplificando la gestión de recursos de Cloudflare a través de un sencillo conjunto de comandos Python.

## Estructura del Proyecto

```
netspresso/
│
├── cloudflare/
│ ├── cloudflare/
│ │ ├── init.py
│ │ └── cloudflare.py
│ │
│ ├── tests/
│ │ └── test_cloudflare.py
│ │
│ ├── .env
│ └── requirements.txt
└── ejecutar_cloudflare.sh
```


## Configuración

### Requisitos

- Python 3.6+
- Pip (Gestor de paquetes de Python)

### Instalación

1. Clona el repositorio:

`git clone [URL del repositorio]`

2. Navega al directorio del proyecto:

`cd netspresso`

3. Instala las dependencias:

`pip install -r cloudflare/requirements.txt`


### Configuración de Variables de Entorno

1. Crea un archivo `.env` en el directorio `cloudflare/` con las siguientes variables:

```
CLOUDFLARE_API_KEY=[tu_api_key_aquí]
CLOUDFLARE_EMAIL=[tu_email_aquí]
```

Reemplaza `[tu_api_key_aquí]` y `[tu_email_aquí]` con tus credenciales de Cloudflare.

## Uso

Para ejecutar el módulo Cloudflare y realizar operaciones con la API, utiliza el script `ejecutar_cloudflare.sh` en la raíz del proyecto. Este script configura el entorno y ejecuta el módulo principal.

## Pruebas

Para ejecutar las pruebas unitarias, asegúrate de estar en el directorio raíz del proyecto y ejecuta:

`python -m unittest cloudflare/tests/test_cloudflare`


## Contribuciones

Las contribuciones al proyecto son bienvenidas. Por favor, asegúrate de seguir las mejores prácticas de desarrollo y mantener el código bien documentado.

## Licencia

MIT

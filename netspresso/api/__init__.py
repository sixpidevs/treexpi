# netspresso/api/__init__.py

# Importaciones desde los módulos internos
from .cloudflare import list_zones, create_dns_record, delete_dns_record
from .models import Zone, DNSRecord

# Con estas importaciones, puedes acceder a list_zones, create_dns_record,
# delete_dns_record, Zone y DNSRecord directamente a través de netspresso.api

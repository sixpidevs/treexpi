# netspresso/api/models.py

class Zone:
    """Representa una zona DNS en Cloudflare."""

    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_dict(cls, data):
        """Crear una instancia de Zone a partir de un diccionario."""
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            status=data.get("status")
        )


class DNSRecord:
    """Representa un registro DNS en una zona de Cloudflare."""

    def __init__(self, id, type, name, content, zone_id):
        self.id = id
        self.type = type
        self.name = name
        self.content = content
        self.zone_id = zone_id

    @classmethod
    def from_dict(cls, data):
        """Crear una instancia de DNSRecord a partir de un diccionario."""
        return cls(
            id=data.get("id"),
            type=data.get("type"),
            name=data.get("name"),
            content=data.get("content"),
            zone_id=data.get("zone_id")
        )

    def to_dict(self):
        """Convertir la instancia de DNSRecord a diccionario."""
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "content": self.content,
            "zone_id": self.zone_id
        }

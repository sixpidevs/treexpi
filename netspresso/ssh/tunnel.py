# netspresso/ssh/tunnel.py

import paramiko
from paramiko import SSHClient
from contextlib import contextmanager

class SSHTunnelManager:
    def __init__(self, host, port, username, key_file):
        self.host = host
        self.port = port
        self.username = username
        self.key_file = key_file
        self.client = None

    def connect(self):
        """Establece una conexión SSH al servidor."""
        self.client = SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, self.port, self.username, key_filename=self.key_file)

    def close(self):
        """Cierra la conexión SSH."""
        if self.client:
            self.client.close()

    @contextmanager
    def tunnel(self, local_port, remote_host, remote_port):
        """
        Crea un túnel SSH desde un puerto local a un host remoto y puerto.

        Uso:
            with SSHTunnelManager(...).tunnel(8080, 'remote_host', 80) as tunnel:
                # Acciones mientras el túnel está activo
        """
        try:
            self.connect()
            transport = self.client.get_transport()
            channel = transport.open_channel("direct-tcpip", (remote_host, remote_port), ("127.0.0.1", local_port))
            yield channel
        finally:
            self.close()

# Ejemplo de cómo utilizar la clase SSHTunnelManager
if __name__ == "__main__":
    # Estos valores deberán ser reemplazados por tus propios datos de conexión SSH
    host = "tu_servidor_ssh.com"
    port = 22
    username = "tu_usuario"
    key_file = "/ruta/a/tu/llave/privada"

    tunnel_manager = SSHTunnelManager(host, port, username, key_file)
    with tunnel_manager.tunnel(8080, "remote_host", 80):
        print("Túnel SSH establecido. Se puede acceder al host remoto a través del puerto local 8080.")

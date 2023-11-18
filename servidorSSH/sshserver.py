import paramiko


def create_ssh_tunnel():
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Reemplaza con tus propios detalles de conexión
        ssh_client.connect(
            hostname="SSH_SERVER_HOSTNAME",
            port=22,
            username="USERNAME",
            key_filename="PATH_TO_PRIVATE_KEY",
        )

        # Configuración del reenvío de puertos:
        # Reenvía el puerto 8080 de tu máquina local al puerto 8000 del servidor remoto
        tunnel = paramiko.SSHTunnelForwarder(
            (ssh_client.get_transport().sock.getpeername()[0], 22),
            ssh_host_key=None,
            ssh_username="USERNAME",
            ssh_private_key="PATH_TO_PRIVATE_KEY",
            remote_bind_address=("127.0.0.1", 8000),
            local_bind_address=("0.0.0.0", 8080),
        )

        tunnel.start()
        print(
            "Túnel SSH establecido. Conectar a localhost:8080 para acceder al servidor remoto."
        )

        return tunnel
    except Exception as e:
        print(f"Error al establecer el túnel SSH: {e}")


if __name__ == "__main__":
    ssh_tunnel = create_ssh_tunnel()
    try:
        # Mantén el script corriendo para mantener el túnel abierto
        input("Presiona Enter para terminar...")
    finally:
        print("Cerrando túnel SSH...")
        ssh_tunnel.close()

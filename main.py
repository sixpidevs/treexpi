import threading
from servidorHTTS.httpserver import run_server
from servidorSSH.sshserver import create_ssh_tunnel
from sockets.sockets import main as socket_main


def main():
    # Iniciar el servidor HTTP en un hilo separado
    threading.Thread(target=run_server, daemon=True).start()

    # Establecer la conexión SSH y configurar el reenvío de puertos
    # Suponiendo que esto no necesita ejecutarse en un hilo separado
    create_ssh_tunnel()

    # Iniciar el servidor de sockets
    # Suponiendo que esto no necesita ejecutarse en un hilo separado
    socket_main()


if __name__ == "__main__":
    main()

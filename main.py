import threading
import servidorHTTS
import servidorSSH
import sockets

def main():
    # Iniciar el servidor HTTP en un hilo separado
    threading.Thread(target=servidorHTTS.run_server, daemon=True).start()

    # Establecer la conexión SSH y configurar el reenvío de puertos
    servidorSSH.create_ssh_tunnel()

    # Iniciar el servidor de sockets
    sockets.main()

if __name__ == '__main__':
    main()
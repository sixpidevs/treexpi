import socket

def forward_data(source_sock, target_sock):
    while True:
        source_data = source_sock.recv(1024)
        if not source_data:
            break
        target_sock.send(source_data)

def handle_client(client_socket):
    # Establece conexión con el destino a través del túnel SSH
    remote_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_sock.connect(('localhost', 8080))  # Conexión al túnel SSH

    # Reenvía los datos entre cliente y destino
    forward_data(client_socket, remote_sock)

    # Cierra las conexiones
    client_socket.close()
    remote_sock.close()

def main():
    local_port = 8081  # Puerto local donde escuchar

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', local_port))
    server_socket.listen(5)

    print(f"Escuchando en 0.0.0.0:{local_port}, reenviando a localhost:8080")

    while True:
        client_socket, addr = server_socket.accept()
        handle_client(client_socket)

if __name__ == '__main__':
    main()

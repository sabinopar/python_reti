import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)

    print("Server in ascolto...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connessione da {address} è stata stabilita!")

        message = "Benvenuto nel server!"
        client_socket.send(message.encode())

        client_socket.close()

start_server()
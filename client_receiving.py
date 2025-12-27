import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = client_socket.recv(1024).decode()
    print(f" Messaggio dal server: {message}")

    client_socket.close()

start_client()
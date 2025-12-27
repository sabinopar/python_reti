import socket

# Crea un oggetto socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Si connette al server
client_socket.connect(('localhost', 12345))

print("Connesso al server!")

# Chiude la connessione
client_socket.close()
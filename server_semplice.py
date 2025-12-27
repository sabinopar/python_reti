import socket

# Crea un oggetto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Collega il socket a un indirizzo e porta specifici
server_socket.bind(('localhost', 12345))

# Ascolta le connessioni in arrivo
server_socket.listen(1)

print("Server in ascolto...")

# Accetta una connessione
client_socket, address = server_socket.accept()
print(f"Connessione da {address} è stata stabilita!")

# Chiude la connessione
client_socket.close()
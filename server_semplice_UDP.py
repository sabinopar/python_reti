import socket

# Crea un oggetto socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Collega il socket a un indirizzo e porta specifici
server_socket.bind(('localhost', 9998))

# rRiceve dal client
data, addr = server_socket.recvfrom(1024)

print("Ricevuto:", data.decode("utf-8"), "da", addr)
messaggio_risposta = "Messaggio:" + str(data) + " ricevuto. " + "Saluti dal Server"

# Invia risposta al client
server_socket.sendto(bytes(messaggio_risposta, "utf-8"), addr)

# Chiude la connessione
server_socket.close()
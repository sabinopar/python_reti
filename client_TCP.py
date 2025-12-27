import socket

target_host = "0.0.0.0"
target_port = 9998

# creazione oggetto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connessione del client
client.connect((target_host, target_port))

# invio dei dati
client.send(b"test")

# ricezione della risposta
response = client.recv(4096)

print(response.decode())

client.close()
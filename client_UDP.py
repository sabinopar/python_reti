import socket

target_host = "0.0.0.0"
target_port = 9998

# creazione oggetto socket
# per il client UDP il socket è SOCK_DGRAM
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# invio dei dati al server, fornendo il messaggio e il server target
client.sendto(b"test", (target_host, target_port))

# ricezione della risposta
data, addr = client.recvfrom(4096)

print(data.decode())

client.close()
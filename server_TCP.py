# SERVER TCP
import socket
import threading

IP = "0.0.0.0"
PORT = 9998


def main():
    # creiamo il socket
    # AF_INET indica che usiamo un indirizzo IPv4 o un nome host
    # SOCK_STREAM indica che il tipo di socket è TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # passiamo IP  e porta su cui il server sia in ascolto
    server.bind((IP, PORT))
    # il server è in attesa e accetta fino a massimo 5 connessioni
    server.listen(5)
    print("In ascolto su", IP,":",PORT)
    
    # in attesa di connessione in entrata
    while True:
        # a connessione avvenuta si conservano il socket client e i dettagli della connessione
        client, address = server.accept()
        print("Accettata connessione da", address[0],":",address[1])
        # creiamo un nuovo oggetto Thread agganciato alla nostra funzione 'handle_client' che riceve come argomento il socket client
        client_handler = threading.Thread(target=handle_client, args=(client, ))
        # il thread potrà accuparsi della nuova connessione del client e il server potrà tornare in attesa di una nuova chiamata
        client_handler.start()
        
def handle_client(client_socket):
    with client_socket as sock:
        
        # riceve dal client
        request = sock.recv(1024)
        print("Ricevuto:", request.decode("utf-8"))
        
        # invia risposta al client
        sock.send(b"ACK")
main()
    
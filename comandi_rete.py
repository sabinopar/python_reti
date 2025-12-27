import os

# comandi di rete con il kernel Linux

result = os.system("ifconfig -a")

url = input("Inserisci l'URL o l'IP di una macchina per effettuare il 'ping': ")
result = os.system("ping -c 3 " + url)


url = input("Inserisci l'URL o l'IP di una macchina per visualizzare gli eventi lungo il percorso: ")
result = os.system("traceroute " + url)


url = input("Inserisci l'URL o l'IP di una macchina per trovare l'IP associato o il nome di dominio (comando 'host'): ")
result = os.system("host " + url)

# tabella di instradamento
result = os.system("route" )

import socket

SRV_ADDR = "192.168.0.194" #Indirizzo IP ottenuto da terminale con "ip a"
SRV_PORT = 44445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #predisponiamo il socket (socket.AF_INET dico che è un IPv4, socket.SOCK_STREAM dico che)
s.bind((SRV_ADDR, SRV_PORT)) #assegna ip e la porta al socket (dentro bind passiamo i valori IP e "porta usata")
s.listen(1) #indica 

print(f"Server in ascolto alla porta: {SRV_PORT}")
connection, address = s.accept() #addres = indirizzo ip di chi ci contatta, connection = dati che arrivano (s.accept() serve per )
print(f"Siamo stati contattati da {address}")

while True: #faccio un ciclo infinito
    data = connection.recv(64)
    #if not data: break #se non arrivano dati esci dal ciclo
    if data == b'exit\n': break #se arriva exit in dati grezzi chiudi la comunicazione
    connection.sendall(b'Messaggio ricevuto\n') #serve ha mandare un messaggio di conferma di ricezione messaggio al mittente
    print(data.decode('UTF-8')) #data.decode('UTF-8') serve a decodificare i dati che arrivano in dati legibili

connection.close() #chiudo la porta, interrompo la connessione
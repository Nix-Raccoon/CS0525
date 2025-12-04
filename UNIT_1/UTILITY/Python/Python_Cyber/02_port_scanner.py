import socket
#IN QUESTO SCRIPT ANDIAMO A SCANSIONARE UNA LISTA DI PORTE DI UN INDIRIZZO IP
target = input("IP da scansionare: ")
portrange = input("Range delle porte (es 20-100): ")

lowport = int(portrange.split('-')[0]) #splittiamo a partire del trattino e prendiamo il primo numero trasformandoli in int -> 20
highport = int(portrange.split('-')[1]) #splittiamo a partire del trattino e prendiamo il primo numero trasformandoli in int -> 100

print(f"Scannerizzando l'IP {target} da porta {lowport} a porta {highport}")

for port in range(lowport, highport + 1):#
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#reo il socket
    status = s.connect_ex((target, port)) #connect() da un errore e blocca il programma, connect_ex() da l'errore ma non ferma la macchina. Una funzione che connette due macchine inserendo ip e porta
    if(status == 0): #controllo se connect_ex() mi restituisce 0 (porta Aperta) mi restituisce 1(porta Chiusa)
        print(f"Porta {port}: APERTA")
    else:
        print(f"Porta {port}: CHIUSA")   
    s.close()     


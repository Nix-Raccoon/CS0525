#Metodo con lista e tutorial
import datetime

lista_comandi = [0, 1, 2] #0 = data, 1 = ora, 2 = nome.

def main():
    tutorial_comandi()
    while True:
        comando_utente = input("Cosa vuoi sapere? ")
        
        if comando_utente == "esci":
            print("Arrivederci!")
            break
        else:
            print(assistente_virtuale(comando_utente))

def assistente_virtuale(comando):
    if comando == "0":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "1":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "2":
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
        tutorial_comandi()
    return risposta

def tutorial_comandi(): #creo una funzione che spara una lista di comandi disponibile da usare all'inizio del programma e qualora si commettesse un errore.
    print('ELENCO COMANDI \n 0 = data \n 1 = ora \n 2 = nome \n "esci" per uscire dal programma')

if __name__ == "__main__":
    main()  














#Metodo 1 (Più pulito ed efficente)
# import datetime

# def main():
#     while True:
#         comando_utente = input("Cosa vuoi sapere? ")
#         if comando_utente == "esci":
#             print("Arrivederci!")
#             break
#         else:
#             print(assistente_virtuale(comando_utente))

# def assistente_virtuale(comando):
#     if comando == "Qual è la data di oggi?":
#         oggi = datetime.date.today()
#         risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
#     elif comando == "Che ore sono?":
#         ora_attuale = datetime.datetime.now().time()
#         risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
#     elif comando == "Come ti chiami?":
#         risposta = "Mi chiamo Assistente Virtuale"
#     else:
#         risposta = "Non ho capito la tua domanda."
#     return risposta
     
# if __name__ == "__main__":
#     main()   


#Metodo 2 (Struttura semplice e diretta)
# import datetime
   
# def assistente_virtuale(comando):
#     if comando == "Qual è la data di oggi?":
#         oggi = datetime.date.today()
#         risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
#     elif comando == "Che ore sono?":
#         ora_attuale = datetime.datetime.now().time()
#         risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
#     elif comando == "Come ti chiami?":
#         risposta = "Mi chiamo Assistente Virtuale"
#     else:
#         risposta = "Non ho capito la tua domanda."
#     return risposta

# while True:
#     comando_utente = input("Cosa vuoi sapere? ")
#     if comando_utente == "esci":
#         print("Arrivederci!")
#         break
#     else:
#         print(assistente_virtuale(comando_utente))


      
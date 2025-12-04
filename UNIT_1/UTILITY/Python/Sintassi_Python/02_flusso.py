#Scrivi un programma che chieda un numero all'utente e determini se è pari o dispari

number = input("Inserisci un numero: ")

if(number.isdigit()):
    number = int(number)
    
    if number % 2 == 0: #se ha resto o meno
        print("Numero pari")
    else:
        print("Numero dispari")

    if number < 10:
        print("Minore di 10")    
    elif number < 20: 
        print("Minore di 20")  
    else:
        print("Numero maggiore o uguale a 20")  
else:
    print("Non è un numero!!")   

print("Fine programma")    
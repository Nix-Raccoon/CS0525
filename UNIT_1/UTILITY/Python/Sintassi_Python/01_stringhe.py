saluto = "Hello World!"
testo1 = "l'amica di Gigi"
testo2 = 'Gigi ha detto: "Non so che dire"'

#Escaping di caratteri speciali con \
testo3 = 'l\'amica di Gigi ha detto "non so che dire"'

#Formattazione di stringa
name = 'Gigi'
print(f"Ciao {name} come stai?") #stringa formattata

print(saluto)

print(testo1)
print(testo2)
print(testo3)

testo_lungo = '''
ciao
come
state
tutto
bene?
'''

print(testo_lungo)

#Cambiare la terminazione end


#Concatenazione di stringhe
print()
print('CONCATENAZIONE')
stringa1 = 'Ciao'
stringa2 = 'a'

stringa_concatenata = stringa1 + ' ' + stringa2 + ' tutti'
print(stringa_concatenata)

print(f"{stringa1} {stringa2} tutti")

#Conversione 
result = 100
print("Il risultato è " + str(result))
print(f"Il risultato è {result}")

#Metodi delle stringhe
print()
print('METODI STRINGHE')

stringa = 'ciao a tutti quanti come state'
stringa.split()

print(stringa.split())
print(stringa.split(sep = "a"))

print(stringa.upper()) #tutto in maiuscolo
print(stringa.lower()) #tutto in minuscolo

string_user = input("Inserisci un numero: ")
print(string_user.isdigit())#solo numeri
print(string_user.isnumeric())#include caratteri speciali
print(string_user.isdecimal())
print(string_user.isalpha())#solo lettere
print(string_user.isalnum())#lettere e numeri


#commento mono-riga

'''
commento
multi-riga 
'''



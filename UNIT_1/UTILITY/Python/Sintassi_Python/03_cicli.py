#CICLO WHILE

# valore = input('Valore (0 per uscire): ') #con stringa

# while valore != '0':
#     print('ciao')
#     valore = input('Valore(0 per uscire): ')



# numero = input('Inserisci un numero: ')   

# while not numero.isdigit(): #OPPURE while numero.isdigit() == False
#     numero = input('Deve essere un numero! Inserisci un numero: ')

# numero = int(numero)

# print(numero / 2)

#CICLO FOR

# for numero in range(10):
#     print(f"5 * {numero} = {5 * numero}")


lista_spesa = [
    "pasta",
    "uova",
    "pane",
    "pomodori"
]

print(lista_spesa)
print(lista_spesa[2])

for cibo in lista_spesa:
    print(cibo)

print(f"Il totale di cose da comprare: {len(lista_spesa)}")    

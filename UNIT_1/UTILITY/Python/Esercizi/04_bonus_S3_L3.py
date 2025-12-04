import re


#ESERCITAZIONE1: DI UNA LISTA DI NUMERI CREARE UNA LISTA DI MEDIE FATTE DA GRUPPI DI TRE CHE SLIDANO DI UNO OGNI VOLTA(SI PARTE DA [1], [1, 2],[1, 2, 3],[2, 3, 4]...)
print('INIZIO PROGRAMMA 1' \
'')

def calculate_group_mean(the_list, start, end): #Creiamo una funzione che andrà a calcolare una media in cui passeremo: la lista, index di inizio e index di fine 
    group = the_list[start : end] #Questo è lo "slicing" di lista (Prende una porzione di the_list, a partire dall’indice start incluso, fino all’indice end escluso)
    mean = sum(group) / len(group) #Calcolo della media: somma ogni valore di group e divide per il totale dei valori che costituiscono group (se group = [2, 4, 6] allora farà (2 + 4 + 6)/3
    return mean #dico che la funzione deve restituire il valore mean


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window = 3

mean_values = [] #lista delle medie calcolate

for index in range(window - 1): #per i gruppi con elementi < di window
    mean_values.append(calculate_group_mean(numbers, 0, index + 1))

for index in range(len(numbers) - window + 1):#per i gruppi con n. elementi = a window
    mean = calculate_group_mean(numbers, 0, index + window)
    mean_values.append(mean)

print(mean_values)    


print('' \
'FINE PROGRAMMA 1')




#ESERCITAZIONE2: IMMETTERE UN TESTO, SETTARLO IN MINUSCOLO, PULIRLO DA CARATTERI SPECIALI E CONTEGGIARE LE PAROLE.
print('INIZIO PROGRAMMA CONTEGGIO PAROLE' \
'')

text =  "Ciao, ciao! Come stai? Stai bene?"

lower_text = str.lower(text) #setto il testo in minuscolo

clean_text = re.sub(r'[^ \w\s]', '', lower_text) #uso Regex per poter includere SOLO i caratteri che voglio usare

#Divido il testo in parole singole con la funzione split()
words = clean_text.split()

#creo un dizionario
dizionario = {}

#per ogni parola nella frase dimmi il quantitativo di parole uguali
for word in words:
     if word in dizionario:
         dizionario[word] += 1
     else:
         dizionario[word] = 1   
        
print(dizionario)

print('' \
 'FINE PROGRAMMA CONTEGGIO PAROLE')
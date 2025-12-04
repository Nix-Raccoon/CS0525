import math

#SCRIVERE UN PROGRAMMA CHE PERMETTA DI FAR SCEGLIERE ALL'UTENTE UNA FIGURA GEOMETRICA, LE MISURE E CHE RESTITUISCA IL VALORE DEL PERIMETRO.

#V2.0
 
figura_geometrica = input('Inserisci figura geometrica (0 = quadrato, 1 = cerchio, 2 = rettangolo): ')

def input_loader():
    if int(figura_geometrica) == 0:
        lato = float(input('Inserisci la misura del lato: '))
        return lato
    elif int(figura_geometrica) == 1:
        raggio = lato = float(input('Inserisci la misura del raggio: '))
        return raggio
    elif int(figura_geometrica) == 2: 
        base = float(input('Inserisci la misura della base: '))
        altezza = float(input('Inserisci la misura dell\'altezza: '))
        return base, altezza
    else:
        print('Questa non è una figura, inserisci una figura!')
        exit() 

def perimetro_cerchio(raggio):   
    perimetro_figura = 2 * math.pi * raggio 
    return perimetro_figura

def perimetro_quadrato_rettangolo(base, altezza): 
    perimetro_figura = (base * 2.0) + (altezza * 2.0)
    return perimetro_figura

    


if int(figura_geometrica) == 0:
    input_lato = input_loader()
    risultato = perimetro_quadrato_rettangolo(float(input_lato), float(input_lato))#calcolo quadrato
    
elif int(figura_geometrica) == 1:
    input_raggio = input_loader()
    risultato = perimetro_cerchio(float(input_raggio))#calcolo cerchio
elif int(figura_geometrica) == 2:
    input_base, input_altezza = input_loader()
    risultato = perimetro_quadrato_rettangolo(input_base, input_altezza) #calcolo rettangolo
else:
    risultato = print('Errore')
        

  
print(f'perimetro = {risultato}')  


#V1.0

# figura_geometrica = input('Inserisci figura geometrica: ')

# if figura_geometrica == 'quadrato':
#     misura_lato = float(input('Inserisci misura del lato: '))
#     perimetro_figura = misura_lato * 4
#     print(f'Il perimetro è di {perimetro_figura}!')
# elif figura_geometrica == 'cerchio':
#     misura_raggio = float(input('Inserisci la misura del raggio: '))   
#     perimetro_figura = 2 * math.pi * misura_raggio
#     print(f'La circonferenza è di {perimetro_figura}!')
# elif figura_geometrica == 'rettangolo':
#     misura_base = float(input('Inserisci la misura della base: '))  
#     misura_altezza = float(input('Inserisci la misura dell\'altezza: '))  
#     perimetro_figura = (misura_base * 2) + (misura_altezza * 2)
#     print(f'Il perimetro è di {perimetro_figura}!')
# else:
#     print('Questa non è una figura, inserisci una figura!')  





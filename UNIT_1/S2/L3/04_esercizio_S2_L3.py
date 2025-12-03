city = input('Inserisci il nome della città: ')

while city.isalpha() != True:
    city = input('Inserisci solo lettere! Nome della città')



pet_name = input('Inserisci il nome del tuo animale domestico: ')

while pet_name.isalpha() != True:
    pet_name = input('Inserisci solo lettere! Nome dell\'animale domestico') 


band_name = f"Il nome della tua band è: {city} {pet_name} " 

print(band_name)

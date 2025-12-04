import http.client

host = input('Inserire IP: ')
port = input('Inserire la porta (default: 80): ')

if port == '':
    port = 80
else:
    port = int(port)

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request('GET', '/') #RICHIESTA AL SERVER: (Tipo richiesta, path delle risorse del servizio http) / fa riferimento alla home {tipi richiesta: GET, PUT, OPTIONS ...}
    response = connection.getresponse() #Risposta dal server

    body_bytes = response.read() #mi legge il contenuto di una pagina web allo stato grezzo (in Bytes)
    body_string = body_bytes.decode('utf-8', errors='replace') #Decodifica il codice in Bytes grezzo in una stringa leggibile ignora eventuali caratteri che non possono essere decodificati con il codice 'utf-8'

    print(f'body_bytes è {body_bytes}')
    print(f'body_string è {body_string}')

    connection.close()
except ConnectionRefusedError:
    print("Connessione fallita") 

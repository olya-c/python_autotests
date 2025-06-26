import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5f5307e284cfc9be744f64ac5c45dd01'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
 
body_create = {
    "name": "Рони",
    "photo_id": 1
}  
body_create = {
    "pokemon_id": "289470",
    "name": "Ron",
    "photo_id": 1
} 
body_create = {
    "pokemon_id": "289471"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''  

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)  

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_create)
print(response_create.text) 
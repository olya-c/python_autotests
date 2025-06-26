import requests 
import pytest 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5f5307e284cfc9be744f64ac5c45dd01'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 36225 

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200 

def test_trainer_name_in_response():
    response = requests.get(url=f'{URL}/trainers/{TRAINER_ID}')
    data = response.json()
    assert 'trainer_name' in data, "стиф" 


@pytest.mark.parametrize('key, value', [('name', 'Рони'),('id', '330740')])
def test_parametrize(key, value): 
    response_parametrize = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value 

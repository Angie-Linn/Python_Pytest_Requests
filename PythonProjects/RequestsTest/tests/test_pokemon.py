import requests
import pytest
host = 'https://api.pokemonbattle.me:9104'
token = 'токен'
def test_status_code():
    response= requests.get(f'{host}/trainers', params = {'trainer_id' :1873})
    assert response.status_code == 200

def test_part_of_answer():
    response= requests.get(f'{host}/trainers', params = {'trainer_id' :1873})
    assert response.json()['name'] == 'мяу'
import requests
host = 'https://api.pokemonbattle.me:9104'
token = 'токен'
'''response_add_pokemon = requests.post(f'{host}/pokemons', json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token } )
print (response_add_pokemon.text) '''



'''response_change_pokemon = requests.put(f'{host}/pokemons', json={
    "pokemon_id": "5662",
    "name": "meow",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token } )
print (response_change_pokemon.text)'''


response_pokeball_pokemon = requests.post(f'{host}/trainers/add_pokeball', json={
    "pokemon_id": "5662"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token } )
print (response_pokeball_pokemon.text)
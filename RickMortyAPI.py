# Rick and Morty API
# https://rickandmortyapi.com/documentation/#rest

# Tutorial from John Watson Rooney YouTube channel

import requests
import pandas as pd

base_url = 'https://rickandmortyapi.com/api/'
endpoint = 'character'


def main_request(base_url, endpoint, x):
    r = requests.get(base_url + endpoint + f'?page={x}')
    return r.json()

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    character_list = []
    for item in response['results']: 
        character = {
            'id': item['id'], 
            'name': item['name'], 
            'no_of_episodes': len(item['episode']),
        }

        character_list.append(character)

    return character_list


main_list = []
data = main_request(base_url, endpoint, 2)
for x in range(1, get_pages(data) + 1):
    print(x)
    main_list.extend(parse_json(main_request(base_url, endpoint, x)))

df = pd.DataFrame(main_list)
print(df.head(), df.tail())
df.to_csv('RickMorty-Characters.csv', index=False)
print('Saved items to CSV file.')

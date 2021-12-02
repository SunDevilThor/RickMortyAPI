# OFFLINE file for Rick & Morty API py file

import json

with open('characters.json', 'r') as file:
    file = file.read()

data = json.loads(file)

pages = data['info']['pages']

name = data['results'][0]['name']

episodes = data['results'][0]['episode']

print(len(episodes))

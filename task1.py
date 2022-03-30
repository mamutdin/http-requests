import requests
from pprint import pprint

def find_intel(name):
    url = 'https://superheroapi.com/api/2619421814940190/search/' + name
    res = requests.get(url).json()
    id = res['results'][0]['id']

    url = 'https://superheroapi.com/api/2619421814940190/' + id + '/powerstats'
    r = requests.get(url).json()
    intel = r['intelligence']
    return intel

def max_intel(list_char):
    char_dict = {}
    for char in list_char:
        intel = find_intel(char)
        char_dict[char] = int(intel)
    for key, value in char_dict.items():
        if value == max(char_dict.values()):
            return key


t = ['Hulk', 'Captain America', 'Thanos']
print(max_intel(t))


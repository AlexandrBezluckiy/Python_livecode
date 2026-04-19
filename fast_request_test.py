import requests

def test():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    out = response.json()

print(test)
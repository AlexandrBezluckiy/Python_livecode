import requests

def send_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        return {'status': 'error', 'code': response.status_code}
    try:
        response_json = response.json()
    except:




url = 'https://jsonplaceholder.typicode.com/users/1'
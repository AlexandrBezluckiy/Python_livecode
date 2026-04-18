import requests

def send_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        return {'status': 'error', 'code': response.status_code}
    try:
        response_json = response.json()
        return parse_response(response_json)
    except ValueError:
        return {'status': 'error', 'code': 'Invalid JSON'}

def parse_response(response_json):
    json_data = {}
    name = response_json.get('name')
    email = response_json.get('email')
    address = response_json.get('address', {})
    city = address.get('city')

    if not name:
        return {'status': 'error', 'code': 'Name is required'}
    else :
        json_data['name'] = name
    if not email:
        return {'status': 'error', 'code': 'Email is required'}
    else :
        json_data['email'] = email
    if not address:
        return {'status': 'error', 'code': 'Address is required'}
    if not city:
        return {'status': 'error', 'code': 'City is required'}
    else:
        json_data['city'] = city
    return process_request(json_data)

def process_request(json_data):
    new_user = json_data.get('name')
    for item in data_base:
        if new_user == item.get('name'):
            return {'status': 'error', 'code': 'Name is already taken'}
    data_base.append(json_data)
    send_response()
    return send_response()


def send_response():
    return {
        "status": "success",
        "code": 200,
        "message": "Application created"
    }

data_base = []
url = 'https://jsonplaceholder.typicode.com/users/1'

print(send_request(url))
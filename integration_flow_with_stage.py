import requests
import copy

def data_preparation(url, stage):
    response = requests.get(url)
    if response.status_code != 200:
        return {'status': 'error', 'code': response.status_code}
    try:
        response_json = response.json()
    except ValueError:
        return {'status': 'error', 'code': '400', 'message': 'Bad JSON'}
    response_json['stage'] = stage
    temp_json = copy.deepcopy(response_json)
    temp_data['email_temp'] = temp_json.get('email')
    address = temp_json.get('address', {})
    temp_data['city_temp'] = address.get('city')
    return choose_stage(response_json)

def choose_stage(response_json):
    if response_json['stage'] == 'draft':
       response_json['email'] = 'Unknown'
       response_json['address']['city'] = 'Unknown'
    if response_json['stage'] == 'in_progress':
       response_json['address']['city'] = 'Unknown'
    if response_json['stage'] == 'complete':
        pass
    return parce_json(response_json)

def parce_json(json_data):
    order_data = {}
    name = json_data.get('name')
    email = json_data.get('email')
    address = json_data.get('address', {})
    city = address.get('city')
    stage = json_data.get('stage')

    if not name:
        return {'status': 'error', 'code': '400', 'message': 'Field name is required.'}
    else:
        order_data['name'] = name
    if not email:
        return {'status': 'error', 'code': '400', 'message': 'Field email is required.'}
    else:
        order_data['email'] = email
    if not address:
        return {'status': 'error', 'code': '400', 'message': 'Field address is required.'}
    if not city:
        return {'status': 'error', 'code': '400', 'message': 'Field city is required.'}
    else:
        order_data['city'] = city
    if not stage:
        return {'status': 'error', 'code': '400', 'message': 'Field stage is required.'}
    elif stage not in ('draft', 'in_progress', 'complete'):
        return {'status': 'error', 'code': '400', 'message': 'Unknown stage.'}
    else:
        order_data['stage'] = stage
    return process_request(order_data)

def process_request(order_data):
    found = False
    if order_data['stage'] == 'draft':
        for item in data_base:
            if order_data['name'] == item['name']:
                found = True
        if found:
            return {'status': 'error', 'code': '400', 'message': 'User already exists.'}
        data_base.append(order_data)
        return send_response()
    if order_data['stage'] == 'in_progress':
        found = False
        for item in data_base:
            if order_data['name'] == item['name']:
                item['email'] = temp_data.get('email_temp')
                item['stage'] = order_data.get('stage')
                found = True
                return send_response()
        if not found:
            return {'status': 'error', 'code': '400', 'message': 'User not found.'}
    if order_data['stage'] == 'complete':
        found = False
        for item in data_base:
            if order_data['name'] == item['name']:
                item['city'] = temp_data.get('city_temp')
                item['stage'] = order_data.get('stage')
                found = True
                return send_response()
        if not found:
            return {'status': 'error', 'code': '400', 'message': 'User not found.'}

def send_response():
    return {'status': 'success', 'code': '200', 'message': 'Stage successfully.' }

data_base = []
base_url = 'https://jsonplaceholder.typicode.com/users/'
stages = ['draft', 'in_progress', 'complete']
temp_data = {'email_temp': '', 'city_temp': ''}

for id in range (1, 4):
    url = f'{base_url}{id}'
    for stage in stages:
        data_preparation(url, stage)
        print(data_base)
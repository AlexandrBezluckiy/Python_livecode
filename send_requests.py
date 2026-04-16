import requests

def send_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        return {'status': 'error', 'code': response.status_code}
    try:
        response_json = response.json()
    except:
        return {'status': 'error', 'message': 'Invalid JSON'}
    data = process_request(response_json)
    return data

def process_request(response_json):
    json_data = {}
    name = response_json.get("name")
    email = response_json.get("email")
    address = response_json.get("address", {})
    city = address.get("city")

    if not name or name is None:
        return {'status': 'error', 'code': '400', 'message': 'Field name is required.'}
    else:
        json_data['name'] = name
    if not email or email is None:
        return {'status': 'error', 'code': '400', 'message': 'Field email is required.'}
    else:
        json_data['email'] = email
    if address is None:
        return {'status': 'error', 'code': '400', 'message': "Address is required to access city."}
    else:
        json_data['city'] = city
    return json_data

url = 'https://jsonplaceholder.typicode.com/users/1'

print(send_request(url))
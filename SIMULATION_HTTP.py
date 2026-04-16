request_1 = {
    "user_id": 10,
    "action": "create_application",
    "data": {
        "amount": 5000,
        "currency": "USD"
    }
}

request_2 = {
    "user_id": 11,
    "action": "delete_application",
    "data": {}
}

request_3 = {
    "action": "create_application",
    "data": {
        "amount": 1000,
        "currency": "EUR"
    }
}

request_4 = {
    "user_id": 12,
    "action": "create_application"
}

request_5 = {}

request_6 = None

message = {
    'received': "Data received. Status code: 200",
    'processing': "Data in progress.",
    'response error': "Server error response",
    'data error': 'Data error, empty JSON message',
    'validation error': 'Field error',
    'complite': 'Validation complite, in progress'
}

def process_request(request):
    print(message['received'])
    print(message['processing'])

    user = request.get('user_id')
    action = request.get('action')
    data = request.get('data', {})
    amount = data.get('amount')
    currency = data.get('currency')

    if user is None:
        print(message['validation error'])
        return {"status": "error", "code": 400, "message": "user_id required"}
    elif not user:
        print(message['validation error'])
        return {"status": "error", "code": 400, "message": "user_id required"}

    if action is None:
        return {"status": "error", "code": 400, "message": "action required"}
    elif not action:
        return {"status": "error", "code": 400, "message": "action empty"}
    elif action not in ['create_application']:
        return {"status": "error", "code": 400, "message": "Invalid action"}

    if data is None or len(data) == 0 or action:
        print(message['complite'])
        return {"status": "OK", "code": 200, "message": "Message sent successfully"}

def send_request(request):
    if type(request) != dict:
        print(message['response error'])
        return {"status": "error", "code": 400, "message": "Invalid incomming data type"}

    if len(request) == 0:
        print(message['data error'])
        return {"status": "error", "code": 400, "message": "Data error, empty JSON message"}

    response = process_request(request)
    return response

print('Response: ', send_request(request_1))
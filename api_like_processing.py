request = {
    "user_id": 10,
    "action": "create_application",
    "data": {
        "amount": 5000,
        "currency": "USD"
    }
}

def process_request(request):
    if request['action'] == 'create_application':
        result = {"status": "success", "message": "Application created"}
        return result
    else:
        result = {"status": "error", "message": "Unknown action"}
        return(result)

print(process_request(request))
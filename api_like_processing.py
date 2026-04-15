request = {
    "user_id": 10,
    "action": "create_application",
    "data": {
        "amount": 5000,
        "currency": "USD"
    }
}

def process_request(request):
    action = request.get('action')
    if action == 'create_application':
        return {"status": "success", "message": "Application created"}
    else:
        return {"status": "error", "message": "Unknown action"}
    
print(process_request(request))
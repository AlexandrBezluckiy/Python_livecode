request = {
    "user_id": 10,
    "action": "create_application",
    "data": {
        "amount": 5000,
        "currency": "USD"
    }
}

applications = []

def process_request(request):
    action = request.get("action")
    if action == 'create_application':
        data = request.get("data", {})
        user_id = request.get("user_id")

        if not user_id:
            return {"status": "error", "code": 400, "message": "user_id required"}

        app = {
            'user_id': request.get("user_id"),
            'amount': data.get("amount"),
            'currency': data.get("currency")
        }
        applications.append(app)
        return {
            'status': 'success',
            'code': 200,
            'message': 'Application created',
            'user_id': request["user_id"]}
    else:
        return {
            'status': 'error',
            'code': 400,
            'message': 'Unknown action'}

print(process_request(request))
# Задача: Получить ответ в виде
# {
#     "user_id": 10,
#     "action": "create_application",
#     "amount": 5000,
#     "currency": "USD"
# }

request = {
    "user_id": 10,
    "action": "create_application",
    "data": {
        "amount": 5000,
        "currency": "USD"
    }
}

def parse_request(request):
    parse = {}
    for k, v in request.items():
        if isinstance(v, dict):
            for k_in, v_in in v.items():
                parse[k_in] = v_in
        else:
            parse[k] = v
    return parse

print(parse_request(request))

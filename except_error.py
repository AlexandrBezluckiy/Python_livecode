data = {"name": "Alex"}

def get_age_with_if(data):
    if "age" in data:
        return data["age"]
    else:
        return "age not provided"

def get_age_with_try(data):
    try:
        return data['age']
    except (KeyError, TypeError):
        return "age not provided"

print(get_age_with_if(data))
print(get_age_with_try(data))
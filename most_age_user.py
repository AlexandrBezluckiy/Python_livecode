users = [
    {"id": 1, "name": "Alex", "age": 25},
    {"id": 2, "name": "Anna", "age": 17},
    {"id": 3, "name": "John", "age": 30},
    {"id": 4, "name": "Maria", "age": 22},
]

def get_adults(users):
    adult_users = [user for user in users if user.get('age') >= 18]
    return adult_users

def get_user_by_id(users, user_id):
    for user in users:
        if user_id == user.get('id'):
            return user
    return "User not found"


def average_age(users):
    age_sum = sum((user.get('age') for user in users))
    return age_sum / len(users)

print(get_adults(users))

user_id = int(input('Введите id пользователя: '))
print(get_user_by_id(users, user_id))

print(average_age(users))
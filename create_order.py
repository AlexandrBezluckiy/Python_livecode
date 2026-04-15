from copy import deepcopy

applications = []
app = {'name': 'Vesna', 'total': 25}

def create_application(applications, app):
    new_app = deepcopy(app)
    new_app['app_id'] = len(applications) + 1
    applications.append(new_app)
    return new_app

def list_applications(applications):
    return [deepcopy(item) for item in applications]

def find_application(applications, app_id):
    for item in applications:
        if item['app_id'] == app_id:
            return item
    return "not found"

for i in range (10):
    create_application(applications, app)

print(list_applications(applications))

app_id = int(input("Application id: "))
print(find_application(applications, app_id))

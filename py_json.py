# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJson = '{ "first_name" : "Sibtain" , "last_name" : "Raza", "age" : 27 }'

# Parse a dict
user = json.loads(userJson)
# print(user['first_name'])
# print(user)

car = {
    'make': 'Ford',
    'model': "Mustang",
    'year': 1970
}

carJson = json.dumps(car)

print(carJson)

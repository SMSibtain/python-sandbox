# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name': 'Sibtain',
    'last_name': 'Raza',
    'age': 27
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get Value
# print(person['first_name'])
# print(person.get('first_name'))

# Add Key/Value
person['phone'] = '03412414814'

# print(person)

# Get dict keys
# print(person.keys())

# Get dict items
# print(person.items())

# Get dict values
# print(person.values())

# Copy dict
person2 = person.copy()
person2['city'] = 'Karachi'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
# print(len(person2))

# List of dict

people = [
    {'name': 'Sibtain 1', 'age': 21},
    {'name': 'Sibtain 2', 'age': 22}
]

print(people[1]['name'])

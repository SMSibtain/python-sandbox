# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance {self.balance}'

    def set_balance(self, balance):
        self.balance = balance


# Initilialize user object
brad = User('Sibtain', 'smsibtainrn@gmail.com', 27)
brad.has_birthday()

janet = Customer('Janet', 'janet@gmail.com', 30)
janet.set_balance(2500)
print(janet.greeting())

# Extend Class

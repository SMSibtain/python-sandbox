# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# Concatenate
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Argument by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello ,my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize String
print(s.capitalize())
print(s.swapcase())
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

print(s.split())

print(s.isalpha())
print(s.isalnum())
print(s.isnumeric())

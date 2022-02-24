# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core Modules
import datetime
from datetime import date
from time import time

# Pip Modules
from camelcase import CamelCase

# Import Custom Modules
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
# print(c.hump('hello there world'))
# print(validate_email('sibtaingr8@gmail.com'))
# print(timestamp)

email = 'sibtaingr8@gmail.co'
if(validate_email(email)):
    print('Email is valid')
else:
    print('Email is not valid')

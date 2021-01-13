# Ex_33_Wrong.py
from datetime import date


def myfunction():
    return 33, 'John'


year = date.today().year

name = myfunction()

birthyr = year - myfunction()[0]

print(name, 'was born in', birthyr)




# print('Done)
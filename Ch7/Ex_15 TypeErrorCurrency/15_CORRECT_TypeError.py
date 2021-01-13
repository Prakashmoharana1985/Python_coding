# 15_CORRECT_TypeError.py
eur = 'euros'
usd = 3.45
try:
    mymoney = eur + usd
except NameError:
    print("Name error when adding")
except TypeError:
    print("Type error when adding")

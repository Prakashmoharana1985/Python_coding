# 15_WRONG_TypeError.py
eur = 'euro'
gbp = 8
usd = 3.45
try:
    mymoney = eur + usd
    print(mymoney)
except TypeError:
    print('Type error when adding; eur', eur, '; usd', usd)
except Exception as strmsg:
    print(strmsg)

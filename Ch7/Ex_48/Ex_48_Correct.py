# Ex 48 Correct.py

words = ['hello', '1999']
myphrase = 'hello world it is 1999'
mydict = {'words': myphrase}

for word in words:
    if word in myphrase:
        print("It's 1999")

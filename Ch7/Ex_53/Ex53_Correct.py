# Ex_53_Correct.py


def myfunction(i):
    if i > 0:
        return i, 'some text'
    else:
        return i, 'some text'


j = 0
k = ''
j, k = myfunction(-1)

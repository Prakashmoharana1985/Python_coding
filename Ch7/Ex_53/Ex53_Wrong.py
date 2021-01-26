# Ex_53_WRONG.py


def myfunction(i):
    if i > 0:
        return i, 'some text'
    else:
        return False


j = 0
k = ''
j, k = myfunction(-1)

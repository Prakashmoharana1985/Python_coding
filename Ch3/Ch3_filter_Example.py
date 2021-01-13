def myfunc(mystr):
    if mystr in 'Hello':
        return True
    else:
        return False


myvar = ('H', 'i')
print(list(filter(myfunc, myvar)))


myvar = filter(lambda x: x > 4, [1, 3, 6, 7])
print(tuple(myvar))

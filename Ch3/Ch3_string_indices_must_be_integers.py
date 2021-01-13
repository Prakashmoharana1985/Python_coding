mystr = 'abc'
for i in range(len(mystr)):
    print(mystr[i])

# this creates a TypeError
mystr = 'abc'
for i in mystr:
    print(mystr[i])

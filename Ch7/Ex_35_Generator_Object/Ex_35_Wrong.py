# Ex_35_Wrong.py


def genTest():
    yield 1
    yield 2
    print('inside genTest, i is', i)


foo = genTest()

for i in range(3):
    print('item ', foo.__next__())


# print('Done')

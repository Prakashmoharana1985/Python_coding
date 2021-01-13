# sort_itemgetter.py
from operator import itemgetter

mylist = ['blue', 'red', 'Red']
mylist2 = sorted(mylist, key=str.lower, reverse=True)

mylist = [('red', 3), ('Red', 1), ('blue', 2)]
mylist2 = sorted(mylist, key=itemgetter(1, 0))


# print('Done')

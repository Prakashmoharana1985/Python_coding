from collections import defaultdict

mylist = [(1, 'one'), (2, 'two')]
dd = defaultdict(list)  # initial value for default_factory
for k, v in mylist:
    dd[k].append(v)

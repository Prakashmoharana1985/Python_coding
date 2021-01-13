pairs = [(1, 'Jan'), (2, 'Feb'), (3, 'April')]
pairs.sort(key=lambda m: m[1])


for i in map(lambda x: x * 4, [1, 3, 6, 7]):
    print(i)

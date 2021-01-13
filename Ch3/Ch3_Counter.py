from collections import Counter


bills = ['one', 'five', 'ten', 'one']
cnt = Counter()  # create a counter
for i in bills:
    cnt.update([i])
ones = cnt['one']
print('there are %d ones' % (ones))

def c(b, bc=0):
    i = '\nStack '
    j = ' - bc value is'
    k = "'bc' identifier is "
    while bc < len(b):
        bc += 1
        i = i + str(bc + 1) + j + str(bc)
        print(i)
        print(k, id(bc))
        bc = c(b, bc)
    return bc


books = ['bk1', 'bk2', 'bk3']
print('\nStack 1 (global namespace)')
cnt = c(books)
print('\nThere are %d books in %s' % (cnt, books))

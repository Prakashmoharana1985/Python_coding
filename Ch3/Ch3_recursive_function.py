def printbooks(books, bookcnt=0):
    while bookcnt < len(books):
        print(books[bookcnt])
        bookcnt += 1
        bookcnt = printbooks(books, bookcnt)
    return bookcnt


books = ['bk1', 'bk2', 'bk3']
cnt = int(printbooks(books))
print('There are %d books in %s' % (cnt, books))

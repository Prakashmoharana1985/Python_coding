# Generator.py


def nameListGen():
    for i in range(1000000000):
        studentName = 'student_'
        studentName += str(i)
        yield studentName


studentNames = nameListGen()

for j in range(20):
    print(studentNames.__next__())

    print(next(studentNames))

# print('Done')

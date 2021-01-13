# Ex_27_Wrong.py

s1 = [['history'], ['math'], ['social studies']]
s2 = ['Math', None, 'Social Studies']

for c in range(0, 3):
    course1, course2 = '', ''
    course1 = s1[c]
    course2 = s2[c]
    if course1 == course2:
        print('Repeating class: ', course2)
    else:
        print("no match")


# print('Done')
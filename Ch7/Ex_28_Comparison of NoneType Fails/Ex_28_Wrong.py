# Ex_28_Wrong.py

s1 = [['history'], ['math'], ['social studies']]
s2 = ['Math', None, 'Social Studies']

for c in range(0, 3):
    # convert list items to a string
    # [2:-2] slices the new string to remove the
    # opening & closing quotes and brackets
    course1 = str(s1[c])[2:-2].upper()
    course2 = s2[c].upper()
    if course1 == course2:
        print('Repeating class: ', course2)
    else:
        print('no match')


# print('Done')

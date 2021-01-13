# Ex_28_Correct.py

s1 = [['history'], ['math'], ['social studies']]
s2 = ['Math', None, 'Social Studies']

for c in range(0, 3):
    # convert list items to a string
    # [2:-2] slices the new string to remove the
    # opening & closing quotes and brackets
    course1, course2 = '', ''
    try:
        course1 = str(s1[c])[2:-2].upper()
    except Exception:
        course1 = ''
    try:
        course2 = s2[c].upper()
    except Exception:
        course2 = ''
    if course1 == course2:
        print('Repeating class: ', course2)


print('Done')
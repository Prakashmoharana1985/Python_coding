mydictionary = {'Name': 'Zimmerman',
                'Grade': 'A',
                'Course': 'Python Programming'}

mydictionary['Credits'] = '3'

del(mydictionary['Credits'])

for myvalues in mydictionary.values():
    print(myvalues.title())

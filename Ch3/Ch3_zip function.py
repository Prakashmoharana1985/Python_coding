#Ch3 zip function.py

myList = []
x = ['John', 'Mary', 'Herman']
y = [1, 2, 3]
zipped = zip(x, y)
myList = list(zipped)

print(myList)

# to unzip back to original format
a, b = zip(*myList)


# Example 2
# c, g, s, t - course, grade, score, teacher
myDict = {'John': ['Civics', 'A', 94, 'Dr. Brown'],
          'Mary': ['English', 'B', 82, 'Dr. Smith'],
          'Herman': ['Physics', 'C', 70, 'Prof. Stanley']}

c, g, s, t = list(zip(*myDict.values()))
newList = [dict(zip(myDict, col)) for col in zip(*myDict.values())]

graphNums = list(newList[2].values())

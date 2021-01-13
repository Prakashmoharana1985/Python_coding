# Ex2_CORRECT.py
meals = ['breakfast', 'lunch', 'snack', 'dinner']
fruits = ['apple', 'orange', 'grape']

i = 0
j = 0

while i < 4:
    print("my meal is: ",  meals[i])
    while j < 3:
        print("My choice of fruit is: ", fruits[j])
        print("j is: ", j)
        j = j + 1
    i = i + 1

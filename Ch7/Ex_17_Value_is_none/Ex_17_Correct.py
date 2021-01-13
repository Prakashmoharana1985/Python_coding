def mymath(i=5, j=200):
    if i > 3:
        return i*j
    if i < 3:
        return j/i


result = mymath(3, 100)
if result is not None:
    print(result/10)
else:
    print("result is None")

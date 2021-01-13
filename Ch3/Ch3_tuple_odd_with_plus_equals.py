myTuple1 = (1, 2, 3, 4, 5)
myTuple2 = ()
i = 0
while i < len(myTuple1):
    myTuple2 += (myTuple1[i],)
    i += 2



print(myTuple2)
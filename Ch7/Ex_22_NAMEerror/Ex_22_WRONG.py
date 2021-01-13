import matplotlib.pyplot as plot


myL = [13.7, 4.1, 14.4, 23.3, 27, 22, 31.99, 36.2]
bins = [0, 11, 21, 31, 40]
plt.hist(myL, bins, rwidth=0.5)  # histogram graph
plt.xticks([10, 20, 30, 40])
plt.xlabel('age')
plt.ylabel('participants')
plt.show()

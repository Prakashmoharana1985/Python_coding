import matplotlib.pyplot as plot
import statistics


myL = [1.41, 2.3, 1.99, 1.2]
total = str(len(myL))
bins = [1, 2, 3, 4]  # change to whole numbers
bar_width = 0.3
avg = str(round(statistics.mean(myL), 2))
xlbl = total + ' Purchases, Avg: $' + avg
xl = ['Item1', 'item2', 'item3', 'item4']

fig, ax = plot.subplots()

ax.bar(bins, myL, width=.3, color='b')
plot.xticks(bins, xl, color='cornflowerblue')
plot.yticks(color='g')
plot.ylabel('cost', color='g')
plot.xlabel(xlbl, color='g', style='italic')
ax.set_title('Avg Cost Per Purchase', color='r',
             fontweight='bold', fontsize=12)
ax.spines['top'].set_color('y')
ax.spines['bottom'].set_color('y')
ax.spines['left'].set_color('y')
ax.spines['right'].set_color('y')
fig.subplots_adjust(top=1.1)  # add space at top

plot.text(3.6, 1.8, '2020', bbox={'alpha': 0.1})
plot.show()

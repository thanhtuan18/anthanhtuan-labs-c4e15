from matplotlib import pyplot

#1. Chuan bi data
labels = ["Android", "iOS", "Web"]
values = [300, 400, 300]
colors = ["red", "gold", "green"]
explode = [0, 0.2, 0]

#2. Ve (plot)
pyplot.pie(values, labels=labels, colors=colors, explode=explode, shadow=True)
pyplot.axis("equal")

#3. Show
pyplot.show()

from matplotlib import pyplot as plt
from matplotlib import animation as animation
from matplotlib import style

style.use('fivethirtyeight')


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n') ## reading new lines here
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

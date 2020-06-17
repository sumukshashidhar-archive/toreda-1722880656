#this will plot the results live


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import argparse

# styling
style.use('dark_background')

#parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="Add the filepath as a string")
parser.add_argument("-i", "--interval", help="Time in seconds before updates to the graph")
args = parser.parse_args()
inter = args.interval if args.interval!=None else 5000

if args.path == None:
    print("Please pass in the path argument for this to work")
    exit()


file = args.path
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


# main animation function
def animate(i):
    graph_data = open(file,'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=inter)
plt.show()


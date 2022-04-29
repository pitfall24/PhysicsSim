import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from driver import *

firstObject = Object(0, 0, 10, 4, name = 'Test Object')

x = []
y = []

information_needed = ['pos']
firstObject.printinfo()
x.append(firstObject.posx)
y.append(firstObject.posy)

firstObject.setpos(0, 0)
firstObject.setvel(15, 40)
firstObject.setacc(0, -9.81)
x.append(firstObject.posx)
y.append(firstObject.posy)

for _ in range(25):
  firstObject.printinfo(information_needed)
  firstObject.updatevel()
  firstObject.updatepos()
  x.append(firstObject.posx)
  y.append(firstObject.posy)
  
firstObject.printinfo(information_needed)
x.append(firstObject.posx)
y.append(firstObject.posy)

fig = plt.figure()
plt.xlim(0, 170)
plt.ylim(-300, 170)
graph, = plt.plot([], [], 'o')

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames=len(x), interval=200)
plt.show()
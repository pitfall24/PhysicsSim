import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from driver import *

firstObject = Object(0, 0, 10, 4, name = 'First Object', fps = 60)
secondObject = Object(0, -1, 10, 4, name = 'Second Object', fps = 12)
thirdObject = Object(0, -2, 10, 4, name = 'Third Object;, fps = 3)

x = []
y = []

information_needed = ['pos']

firstObject.setvel(1, 8)
firstObject.setacc(0, -9.81)

secondObject.setvel(1, 8)
secondObject.setacc(0, -9.81)
                     
thirdObject.setvel(1, 8)
thirdObject.setacc(0, -9.81)

x.append(firstObject.posx)
y.append(firstObject.posy)

for _ in range(120):
  firstObject.updatevel()
  firstObject.updatepos()
  x.append(firstObject.posx)
  y.append(firstObject.posy)
  
x.append(firstObject.posx)
y.append(firstObject.posy)

x.append(secondObject.posx)
y.append(secondObject.posy)

for _ in range(24):
  secondObject.updatevel()
  secondObject.updatepos()
  for _ in range(5):
    x.append(secondObject.posx)
    y.append(secondObject.posy)

x.append(secondObject.posx)
y.append(secondObject.posy)

x.append(thirdObject.posx)
y.append(thirdObject.posy)
                     
for _ in range(6):
  thirdObject.updatevel()
  thirdObject.updatepos()
  for _ in range(20):
    x.append(thirdObject.posx)
    y.append(thirdObject.posy)
                     
 x.append(thirdObject.posx)
 y.append(thirdObject.posy)


fig = plt.figure()
plt.xlim(0, 5)
plt.ylim(-5, 10)
graph, = plt.plot([], [], 'b.')

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames = len(x), interval = firstObject.dt * 1000)
plt.show()

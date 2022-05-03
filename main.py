import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from driver import *

firstObject = Object(0, 0, 10, 4, name = 'First Object', fps = 300)
secondObject = Object(0, -1, 10, 4, name = 'Second Object', fps = 60)
thirdObject = Object(0, -2, 10, 4, name = 'Third Object', fps = 12)
fourthObject = Object(0, -3, 10, 4, name = 'Fourth Object', fps = 3)

x = []
y = []

information_needed = ['pos']

firstObject.setvel(1, 8)
firstObject.setacc(0, -9.81)

secondObject.setvel(1, 8)
secondObject.setacc(0, -9.81)
                     
thirdObject.setvel(1, 8)
thirdObject.setacc(0, -9.81)

fourthObject.setvel(1, 8)
fourthObject.setacc(0, -9.81)

x.append(firstObject.posx)
y.append(firstObject.posy)

for _ in range(600):
  firstObject.updatevel()
  firstObject.updatepos()
  x.append(firstObject.posx)
  y.append(firstObject.posy)
  
x.append(firstObject.posx)
y.append(firstObject.posy)

x.append(secondObject.posx)
y.append(secondObject.posy)

for _ in range(120):
  secondObject.updatevel()
  secondObject.updatepos()
  for _ in range(5):
    x.append(secondObject.posx)
    y.append(secondObject.posy)

x.append(secondObject.posx)
y.append(secondObject.posy)

x.append(thirdObject.posx)
y.append(thirdObject.posy)
                     
for _ in range(24):
  thirdObject.updatevel()
  thirdObject.updatepos()
  for _ in range(25):
    x.append(thirdObject.posx)
    y.append(thirdObject.posy)
                     
x.append(thirdObject.posx)
y.append(thirdObject.posy)

x.append(fourthObject.posx)
y.append(fourthObject.posy)

for _ in range(6):
  fourthObject.updatevel()
  fourthObject.updatepos()
  for _ in range(100):
    x.append(fourthObject.posx)
    y.append(fourthObject.posy)

x.append(fourthObject.posx)
y.append(fourthObject.posy)


fig = plt.figure()
plt.xlim(0, 5)
plt.ylim(-5, 10)
graph, = plt.plot([], [], 'b.')

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames = len(x), interval = firstObject.dt * 1000)
plt.show()

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from driver import *

firstObject = Object(0, 0, 10, 4, name = 'First Object', fps = 300)
secondObject = Object(0, -1, 10, 4, name = 'Second Object', fps = 60)
thirdObject = Object(0, -2, 10, 4, name = 'Third Object', fps = 12)
fourthObject = Object(0, -3, 10, 4, name = 'Fourth Object', fps = 3)

objects = [firstObject, secondObject, thirdObject, fourthObject]
information_needed = ['pos']
coords = []

for object in objects:
  object.setvel(1, 8)
  object.setacc(0, -9.807)
  
  coords.append((object.posx, object.posy))
  
  for _ in range(object.fps * 2):
    object.updatevel()
    object.updatepos()
    for _ in range(objects[0].fps / object.fps):
      coords.append((object.posx, object.posy))

fig = plt.figure()
plt.xlim(0, 5)
plt.ylim(-5, 10)
graph, = plt.plot([], [], 'b.')

def animate(i):
    graph.set_data(coords[:i+1][0], coords[:i+1][1])
    return graph

ani = FuncAnimation(fig, animate, frames = len(x), interval = firstObject.dt * 1000)
plt.show()

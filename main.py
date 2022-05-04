import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from driver import *

GLOBAL_FPS = 60

firstObject = Object(0, 0, 0, 0, name = 'First Object', fps = GLOBAL_FPS)
secondObject = Object(0, 0, 0, 0, name = 'Second Object', fps = GLOBAL_FPS)
thirdObject = Object(0, 0, 0, 0, name = 'Third Object', fps = GLOBAL_FPS)
fourthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)

testSystem = System(GLOBAL_FPS, 'Test System', firstObject, secondObject, thirdObject, fourthObject)

testSystem.setacc(0, -9.8)
testSystem.setvel(1, 8)
testSystem.setpos_list([(0, 0), (0, -1), (0, -2), (0, -3)])

'''objects = [firstObject, secondObject, thirdObject, fourthObject]
information_needed = ['pos']
coords = []

for object in objects:
  object.setvel(1, 8)
  object.setacc(0, -9.807)
  
  coords.append((object.posx, object.posy))
  
  for _ in range(object.fps * 2):
    object.updatevel()
    object.updatepos()
    for _ in range(int(objects[0].fps / object.fps)):
      coords.append((object.posx, object.posy))

fig = plt.figure()
plt.xlim(0, 5)
plt.ylim(-5, 10)
graph, = plt.plot([], [], 'b.')

x = [i for i, j in coords]
y = [j for i, j in coords]

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames = len(coords), interval = firstObject.dt * 1000)
plt.show()
'''
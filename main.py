import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from driver import *

GLOBAL_FPS = 24

firstObject = Object(0, 0, 0, 0, name = 'First Object', fps = GLOBAL_FPS)
secondObject = Object(0, 0, 0, 0, name = 'Second Object', fps = GLOBAL_FPS)
thirdObject = Object(0, 0, 0, 0, name = 'Third Object', fps = GLOBAL_FPS)
fourthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)
fifthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)
sixthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)
seventhObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)
eigthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)
ninthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)
tenthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)

testSystem = System(GLOBAL_FPS, 'Test System', firstObject, secondObject, thirdObject, fourthObject, fifthObject, sixthObject, seventhObject, eigthObject, ninthObject, tenthObject)
testSystem.setacc_all(0, -9.8)

testSystem.setvel_list([1 for _ in range(10)], [12 - i for i in range(10)])
testSystem.setpos_list([0 for _ in range(10)], [-i / 3 for i in range(10)])

coords = []
runtime = 2.5

while len(coords) < GLOBAL_FPS * len(testSystem.objects) * runtime:
  testSystem.updateposandvel()
  coords += testSystem.returninfo()

fig = plt.figure()
plt.xlim(0, 5)
plt.ylim(-5, 10)
graph, = plt.plot([], [], 'b.')

x = [i for i, j in coords]
y = [j for i, j in coords]

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames = len(coords), interval = 1000 / (GLOBAL_FPS * len(testSystem.objects)))
plt.show()

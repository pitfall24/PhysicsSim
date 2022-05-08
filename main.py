import pygame
from math import copysign
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from driver import *

GLOBAL_FPS = 24

firstObject = Object(0, 0, 0, 0, name = 'First Object', fps = GLOBAL_FPS)
secondObject = Object(0, 0, 0, 0, name = 'Second Object', fps = GLOBAL_FPS)
thirdObject = Object(0, 0, 0, 0, name = 'Third Object', fps = GLOBAL_FPS)
fourthObject = Object(0, 0, 0, 0, name = 'Fourth Object', fps = GLOBAL_FPS)
fifthObject = Object(0, 0, 0, 0, name = 'Fifth Object', fps = GLOBAL_FPS)
sixthObject = Object(0, 0, 0, 0, name = 'Sixth Object', fps = GLOBAL_FPS)
seventhObject = Object(0, 0, 0, 0, name = 'Seventh Object', fps = GLOBAL_FPS)
eigthObject = Object(0, 0, 0, 0, name = 'Eigth Object', fps = GLOBAL_FPS)
ninthObject = Object(0, 0, 0, 0, name = 'Ninth Object', fps = GLOBAL_FPS)
tenthObject = Object(0, 0, 0, 0, name = 'Tenth Object', fps = GLOBAL_FPS)

testSystem = System(GLOBAL_FPS, 'Test System', firstObject, secondObject, thirdObject, fourthObject, fifthObject, sixthObject, seventhObject, eigthObject, ninthObject, tenthObject)
testSystem.setacc_all(0, -9.8)

testSystem.setvel_list([10 for _ in range(10)], [30 - 2 * i for i in range(10)])
testSystem.setpos_list([i * 10 for i in range(10)], [50 for _ in range(10)])

testSystem.setmass(3)
testSystem.setvolume(36)
testSystem.updateradius()

coords = []
runtime = 1

pygame.init()
pygame.display.set_caption('Test')

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill((255, 255, 255))
  pygame.draw.line(screen, (0, 0, 0), (0, SCREEN_HEIGHT - 50), (500, SCREEN_HEIGHT - 50))

  num_objects = testSystem.length

  for object in testSystem.objects:
    if object.posy < 50:
      object.setpos(object.posx, 50)
      object.setvel(0, 0)
      accx = 0
      accy = 0
      object.setacc(accx, accy)
    
    x, y = object.returnpos()
    y = SCREEN_HEIGHT - y
    
    print(object.returnpos(), object.returnvel(), object.returnacc())
    pygame.draw.circle(screen, (0, 0, 255), (x, y), object.radius)

  testSystem.updateposandvel()
  
  clock.tick(GLOBAL_FPS)
  pygame.display.flip()
pygame.quit()

'''
while len(coords) < GLOBAL_FPS * testSystem.length * runtime:
  testSystem.updateposandvel()
  coords += testSystem.returninfo()
'''

'''
fig = plt.figure()
plt.xlim(0, 5)
plt.ylim(-5, 10)
graph, = plt.plot([], [], 'b.')

x = [i for i, j in coords]
y = [j for i, j in coords]

def animate(i):
    graph.set_data(x[:i+1], y[:i+1])
    return graph

ani = FuncAnimation(fig, animate, frames = len(coords), interval = 1000 / (GLOBAL_FPS * testSystem.length))
plt.show()
'''
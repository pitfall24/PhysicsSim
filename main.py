import pygame
from driver import *
#import pyautogui as pag

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

GLOBAL_FPS = 60

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
counter = 1
runtime = 5

pygame.init()
pygame.display.set_caption('Test')

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
mouseX, mouseY = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
zoomX, zoomY = 2, 2
DISPLAY_WIDTH, DISPLAY_HEIGHT = SCREEN_WIDTH // zoomX, SCREEN_HEIGHT // zoomY

BACKGROUND_COLOR1 = (0, 0, 0)         # Black
BACKGROUND_COLOR2 = (255, 255, 255)   # White

OBJECT_COLOR1 = (15, 60, 255)         # Blueish ig?

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

while len(coords) < GLOBAL_FPS * testSystem.length * runtime:
  testSystem.updateposandvel()
  coords += testSystem.returninfo()

running = True
while running:
  for event in pygame.event.get():
    #print(event)
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        mouseX, mouseY = event.pos
      if event.button == 4:
        zoomX += 0.5
        zoomY += 0.5
        print(zoomX, zoomY)
      if event.button == 5:
        if zoomX and zoomY > 0.3:
          zoomX -= 0.2
          zoomY -= 0.2
        elif zoomX or zoomY == 0.1:
          pass
        else:
          zoomX = 0.1
          zoomY = 0.1
        print(zoomX, zoomY)
      DISPLAY_WIDTH, DISPLAY_HEIGHT = SCREEN_WIDTH // zoomX, SCREEN_HEIGHT // zoomY
      display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    if event.type == pygame.MOUSEMOTION and event.buttons[0]:
        mouseX, mouseY = event.pos
  
  display.fill(BACKGROUND_COLOR2)
  pygame.draw.line(display, BACKGROUND_COLOR1, (0, DISPLAY_HEIGHT - 50), (DISPLAY_WIDTH, DISPLAY_HEIGHT - 50))

  num_objects = testSystem.length

  length = len(coords)
  frames = length // 10

  for i in range(10):
    try:
      pygame.draw.circle(display, OBJECT_COLOR1, (coords[i + counter * 10][0], DISPLAY_HEIGHT - coords[i + counter * 10][1]), firstObject.radius)
    except IndexError:
      counter = 1

  '''
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
  '''

  #testSystem.updateposandvel()
  counter += 1
  clock.tick(GLOBAL_FPS)
  
  screen.fill(BACKGROUND_COLOR1)
  screen.blit(display, (mouseX - DISPLAY_WIDTH // 2, mouseY - DISPLAY_HEIGHT // 2))
  
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
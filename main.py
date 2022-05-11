import pygame
from color import *
from driver import *
#import pyautogui as pag

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
DISPLAY_WIDTH, DISPLAY_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
SCALED_WIDTH, SCALED_HEIGHT = DISPLAY_WIDTH // zoomX, DISPLAY_HEIGHT // zoomY

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
scaled = pygame.transform(display, (DISPLAY_WIDTH // zoomx, DISPLAY_HEIGHT // zoomy))
clock = pygame.time.Clock()

running = True
while running:
  # Event Handling
  for event in pygame.event.get():
    # Quit Game
    if event.type == pygame.QUIT:
      running = False
    # Check for click and scroll
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        mouseX, mouseY = event.pos
      if event.button == 4:
        zoomX += 0.5
        zoomY += 0.5
      if event.button == 5:
        if zoomX and zoomY > 0.6:
          zoomX -= 0.5
          zoomY -= 0.5
        else:
          zoomX = 0.1
          zoomY = 0.1
    # Check for drag
    if event.type == pygame.MOUSEMOTION and event.buttons[0]:
        mouseX, mouseY = event.pos
  
  # Calculate coordinates
  coords = {}
  testSystem.updateposandvel()
  for object in testSystem.object:
    if object.posy <= 50:
      object.posy = 50
      object.vely = 0
      object.accy = 0
  for object in testSystem.objects:
    coords{object.name} = [[object.posx, object.posy], object.radius]
  
  clock.tick(GLOBAL_FPS)
  
  screen.fill(COLOR8)
  screen.blit(display, (mouseX - DISPLAY_WIDTH // 2, mouseY - DISPLAY_HEIGHT // 2))
  
  pygame.display.flip()
pygame.quit()

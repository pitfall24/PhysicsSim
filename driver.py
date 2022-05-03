from math import sqrt, sin, cos, atan

GRAVITATIONAL_CONSTANT = 6.6743e-11

class Object:
  def __init__(self, posx, posy, mass, volume, static = False, name = None, fps = 12):
    self.name = name
    self.fps = fps
    self.dt = 1 / fps
    
    self.posx = posx
    self.posy = posy
    
    self.velx = 0
    self.vely = 0
    self.accx = 0
    self.accy = 0
    
    self.mass = mass
    self.volume = volume
    self.density = mass / volume
    
    self.static = static
  
  def setvel(self, newvelx, newvely):
    self.velx = newvelx
    self.vely = newvely
    
  def setpos(self, newposy, newposx):
    self.posy = newposy
    self.posx = newposx
  
  def setacc(self, newaccx, newaccy):
    self.accx = newaccx
    self.accy = newaccy
  
  def updatevel(self):
    self.velx += self.accx * self.dt
    self.vely += self.accy * self.dt
    
  def updatepos(self):
    if self.static == True:
      return
    
    self.posx += self.velx * self.dt
    self.posy += self.vely * self.dt
    
  def printinfo(self, information = ['all']):
    for i in information:
      if i == 'all':
        print('Name:', self.name)
        print('Position (x, y): (' + str(self.posx) + ', ' + str(self.posy) + ')')
        print('Velocity (x, y): (' + str(self.velx) + ', ' + str(self.vely) + ')')
        print('Acceleration (x, y): (' + str(self.accx) + ', ' + str(self.accy) + ')')
        print('Mass (kg): ' + str(self.mass) + 'kg, Volume (m^3): ' + str(self.volume) + 'm^3\n')
      elif i == 'pos':
        print('Position (x, y): (' + str(self.posx) + ', ' + str(self.posy) + ')')
      elif i == 'vel':
        print('Velocity (x, y): (' + str(self.velx) + ', ' + str(self.vely) + ')')
      elif i == 'acc':
        print('Acceleration (x, y): (' + str(self.accx) + ', ' + str(self.accy) + ')')
      elif i == 'mass':
        print('Mass (kg): ' + str(self.mass) + 'kg')

class System:
  def __init__(self, fps, name = None, **kwObjects):
    self.fps = fps
    self.dt = 1 / fps
    self.name = name
    self.objects = {name:object for name, object in kwObjects.items()}
      
  def displayobjects(self):
    for name, object in self.objects.items():
      print('Name:', name, 'Object Name:', object.name)
  
  def updatepos(self):
    for object in self.objects.values():
      object.updatepos()
  
  def updatevel(self):
    for object in self.objects.values():
      object.updatevel()
  
  def setpos(self, newposx, newposy):
    for object in self.objects.values():
      object.setpos(newposx, newposy)
  
  def setvel(self, newvelx, newvely):
    for object in self.objects.values():
      object.setvel(newvelx, newvely)
  
  def setacc(self, newaccx, newaccy):
    for object in self.objects.values():
      object.setacc(newaccx, newaccy)
      
  def updateposvel(self):
    for object in self.objects.values():
      object.updatevel()
      object.updatepos()
        
def calcattraction(object1, object2):
    relx = object1.posx - object2.posx
    rely = object1.posy - object2.posy
    mass1, mass2 = object1.mass, object2.mass
    
    distance = sqrt(relx ** 2 + rely ** 2)
    force = GRAVITATIONAL_CONSTANT * mass1 * mass2 / distance ** 2
    try:
      angle = atan(rely / relx)
    except ZeroDivisionError:
      angle = 0
    
    attractionx = cos(angle) * force
    attractiony = sin(angle) * force
    
    return attractionx, attractiony

def forcetoacc(mass, forcex, forcey):
  accx = forcex / mass
  accy = forcey / mass
  
  return accx, accy

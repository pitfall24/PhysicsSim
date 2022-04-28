from math import sqrt, sin, cos, arctan

GRAVITATION_CONSTANT = 6.6743e-11

class Object:
  def __init__(self, posx, posy, mass, volume, static = False, name = None):
    self.name = name
    
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
  
  def setvel(newvelx, newvely):
    self.velx = newvelx
    self.vely = newvely
    
  def setpos(newposy, newposx):
    self.posy = newposy
    self.posx = newposx
  
  def setacc(newaccx, newaccy):
    self.accx = newaccx
    self.accy = newaccy
  
  def updatevel(accx, accy):
    self.forcex = self.mass / self.accx
    self.forcey = self.mass / self.accy
    
    self.velx += self.accx
    self.vely += self.accy
    
  def updatepos():
    if not self.static:
      return
    else:
      self.posx += self.velx
      self.posy += self.vely
    
  def printinfo():
    print('Name:', self.name)
    print('Position (x, y): (' + str(self.posx) + ', ' + str(self.posy) + ')')
    print('Velocity (x, y): (' + str(self.velx) + ', ' + str(self.vely) + ')')
    print('Acceleration (x, y): (' + str(self.accx) + ', ' + str(self.accy) + ')')
    print('Mass (kg):', self.mass + 'kg, Volume (m^3):', self.volume + 'm^3')

def calcattraction(object1, object2):
    relx = object1.posx - object2.posx
    rely = object1.posy - object2.posy
    mass1, mass2 = object1.mass, object2.mass
    
    distance = sqrt(relx ** 2 + rely ** 2)
    force = GRAVITATIONAL_CONSTANT * mass1 * mass2 / distance ** 2
    angle = arctan(rely / relx)
    
    attractionx = cos(angle) * force
    attractiony = sin(angle) * force
    
    return attractionx, attractiony

def forcetoacc(mass, forcex, forcey):
  accx = forcex / mass
  accy = forcey / mass
  
  return accx, accy

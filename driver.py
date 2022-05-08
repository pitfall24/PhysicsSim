from math import sqrt, sin, cos, atan, pi

GRAVITATIONAL_CONSTANT = 6.6743e-11

class Object:
  def __init__(self, posx, posy, mass, volume, static = False, name = None, fps = 60):
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
    try:
      self.density = mass / volume
    except ZeroDivisionError:
      self.density = 0
    self.radius = sqrt(volume / pi)
    
    self.static = static
    
  def updatepos(self):
    if self.static == True:
      return
    
    self.posx += self.velx * self.dt
    self.posy += self.vely * self.dt

  def updatevel(self):
    self.velx += self.accx * self.dt
    self.vely += self.accy * self.dt

  def updateradius(self):
    self.radius = sqrt(self.volume / pi)
  
  def setpos(self, newposx, newposy):
    self.posx = newposx
    self.posy = newposy

  def setvel(self, newvelx, newvely):
    self.velx = newvelx
    self.vely = newvely
  
  def setacc(self, newaccx, newaccy):
    self.accx = newaccx
    self.accy = newaccy
  
  def returnpos(self):
    return (self.posx, self.posy)

  def returnvel(self):
    return (self.velx, self.vely)

  def returnacc(self):
    return (self.accx, self.accy)

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
  def __init__(self, fps, systemname, *args):
    self.fps = fps
    self.dt = 1 / fps
    self.systemname = systemname
    self.objects = [object for object in args if not object.static]
    self.static_objects = [object for object in args if object.static]
    self.length = len(args)
      
  def displayobjects(self):
    for object in self.objects:
      print('Name: "' + str(object.name) + '"')

  def returninfo(self):
    coords = []

    for object in self.objects:
      coords.append(object.returnpos())

    return coords
  
  def updatepos(self):
    for object in self.objects:
      object.updatepos()
  
  def updatevel(self):
    for object in self.objects:
      object.updatevel()
  
  def setpos_all(self, newposx, newposy):
    for object in self.objects:
      object.setpos(newposx, newposy)

  def setpos_list(self, newposx, newposy):
    if len(self.objects) != (len(newposx) or len(newposy)):
      raise IndexError('Number of objects and new positions do not match')
    if len(newposx) != len(newposy):
      raise IndexError('Number of x and y positions do not match')
    
    for object, posx, posy in zip(self.objects, newposx, newposy):
      object.setpos(posx, posy)
  
  def setvel_all(self, newvelx, newvely):
    for object in self.objects:
      object.setvel(newvelx, newvely)

  def setvel_list(self, newvelx, newvely):
    if len(self.objects) != (len(newvelx) or len(newvely)):
      raise IndexError('Number of objects and new velocities do not match')
    if len(newvelx) != len(newvely):
      raise IndexError('Number of x and y velocities do not match')
    
    for object, velx, vely in zip(self.objects, newvelx, newvely):
      object.setvel(velx, vely)
  
  def setacc_all(self, newaccx, newaccy):
    for object in self.objects:
      object.setacc(newaccx, newaccy)

  def setacc_list(self, newaccx, newaccy):
    if len(self.objects) != (len(newaccx) or len(newaccy)):
      raise IndexError('Number of objects and new accelerations do not match')
    if len(newaccx) != len(newaccy):
      raise IndexError('Number of x and y accelerations do not match')
    
    for object, accx, accy in zip(self.objects, newaccx, newaccy):
      object.setacc(accx, accy)
      
  def updateposandvel(self):
    for object in self.objects:
      object.updatevel()
      object.updatepos()

  def setstatic(self, static):
    for object in self.objects:
      object.static = static

  def setmass(self, newmass):
    for object in self.objects:
      object.mass = newmass
  
  def setvolume(self, newvolume):
    for object in self.objects:
      object.volume = newvolume

  def updatedensity(self):
    for object in self.objects:
      newdensity = object.mass / object.volume
      object.density = newdensity

  def updateradius(self):
    for object in self.objects:
      object.updateradius()
      
  def calcacc(self):
    attraction = {}
    sumx = []
    sumy = []
    
    for object in self.objects:
      for test in self.objects:
        if object == test:
          continue
        else:
          x, y = calcattraction(object, test)
          sumx.append(x)
          sumy.append(y)
      
      avgx = sum(sumx) / len(sumx)
      avgy = sum(sumy) / len(sumy)
      attraction[object] = forcetoacc(object.mass, avgx, avgy)
      sumx.clear()
      sumy.clear()
      
    return attraction
        
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

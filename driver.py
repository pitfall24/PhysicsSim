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
    
  def setvel(velx, vely):
    self.velx = velx
    self.vely = vely
    
  def setpos(posy, posx):
    self.posy = posy
    self.posx = posx
  
  def setacc(accx, accy):
    self.accx = accx
    self.accy = accy
  
  def updatevel(accx, accy):
    self.forcex = mass / accx
    self.forcey = mass / accy
    
    velx += accx
    vely += accy
    
  def updatepos():
    if not static:
      return
    
    posx += velx
    posy += vely
    
  def printinfo():
    print('Name:', name)
    print('Position (x, y): (' + str(posx) + ', ' + str(posy) + ')')
    print('Velocity (x, y): (' + str(velx) + ', ' + str(vely) + ')')
    print('Acceleration (x, y): (' + str(accx) + ', ' + str(accy) + ')')
    print('Mass (kg):', mass + 'kg, Volume (m^3):', volume + 'm^3')

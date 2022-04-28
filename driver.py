class Object:
  def __init__(self, posx, posy, mass, volume, static = False):
    self.posx = posx
    self.posy = posy
    
    self.velx = 0
    self.vely = 0
    
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

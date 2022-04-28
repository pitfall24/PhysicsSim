from driver.py import *

firstObject = Object(0, 0, 10, 4, name = 'Test Object')

firstObject.printinfo()

firstObject.setpos(10, 10)
firstObject.setvel(3, 3)
for _ in range(3):
  firstObject.printinfo()
  firstobject.updatepos()
  
firstObject.printinfo()
firstObject.setacc(-0.5, -0.5)

for _ in range(5):
  firstObject.printinfo()
  firstObject.updatevel()
  firstObject.updatepos()
  
firstObject.printinfo()

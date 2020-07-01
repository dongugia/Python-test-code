import math

class Cricle(object):
    def __init__(self,r):
        self.radius = r
    def area(self):
        return self.radius**2*math.pi
m = float(input("nhập bán kính vào : "))
aCircle =  Cricle(m)
print (round(aCircle.area(),4))
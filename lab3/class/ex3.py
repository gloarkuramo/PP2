from math import pi
class lenght:
    def __init__(self,radius):
        self.radius=radius
    def func(self):
        
        return 2*pi*self.radius
a=int(input())
b=lenght(a)
print(b.func())

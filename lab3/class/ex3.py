from test import shape
class Rectangle(shape):
    def __init__(self, width, length):
        self.width=width
        self.length=length

    def area(self):
        return self.width*self.length
        
a=int(input("width= "))
b=int(input("Length= "))
ex=Rectangle(a,b)
print(ex.area())

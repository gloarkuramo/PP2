class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def show(self):
        return f"{self.x},{self.y}"
    def move(self, x1, x2):
        self.x+=x1
        self.y+=x2
        return f"{self.x},{self.y}"

    def dis(self, dp):
        return ((self.x-dp.x)**2+(self.y-dp.y)**2)**0.5
a=int(input("a= "))
b=int(input("b= "))
p1=Point(a,b)
print(p1.show())
print(p1.move(1,1))
p2=Point(1,1)
print(p1.dis(p2))







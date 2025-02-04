class shape:
    def area(self):
        return 0;
      
class Square(shape):
        def __init__(self, lenght):
            self.lenght=lenght;
        def area(self):
            return self.lenght**2;
a=float(input("a="))

ex=shape()
print(ex.area())
es=Square(a)
print(es.area())


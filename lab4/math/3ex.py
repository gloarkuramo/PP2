from math import pi
from math import tan

p=pi
n=int(input("Input number of sides:"))
a=int(input("Input the length of a side:"))

r=((a/2)/tan(pi/n))


print(((a*n)/2)*r)

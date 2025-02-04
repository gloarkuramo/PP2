def solve(numheads, numlegs):
    res=["Rabits:",0,"and", "Chickens:", 0]
    c=(4*numheads-numlegs)/2
    r=(numlegs-2*numheads)/2
    res[1]=(int(r))
    res[4]=(int(c))
    return res
a=int(input("How many head are there= "))
b=int(input("How many legs are there= "))

print(*solve(a,b))


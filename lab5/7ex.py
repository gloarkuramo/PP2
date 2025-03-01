import re
n=input()

x=n.split("_")
print(x)
t=x[0]
for i in range(1,len(x)):
    t=t+x[i].capitalize()

print(t)

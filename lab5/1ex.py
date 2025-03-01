import re

n=int(input())
a=[]
for i in range(n):
    a.append(input())

res=[]

for i in a:
    t=re.findall("a.*b",i)
    if t:
        res.append(t)
print(res)

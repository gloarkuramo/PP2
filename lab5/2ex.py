import re

n=int(input())
a=[]
for i in range(n):
    a.append(input())

res=[]

for i in a:
    if re.fullmatch(r'ab{2,3}',i):
        print(i,end=" ")

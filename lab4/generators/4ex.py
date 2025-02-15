def firstn(a,b):
    for i in range(a,b+1):
        yield i*i
    
a=int(input())
b=int(input())

for i in firstn(a,b):
    print(i,end=" ")

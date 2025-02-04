def prime(n):
    if n<=1 or n==0:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
    return True
n=int(input())
numbs=[]
for i in range(n):
    t=int(input())
    numbs.append(t)

a=list(filter(lambda x:prime(x), numbs))
print(a)

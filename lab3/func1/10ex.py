def unique(n):
    a=[]
    for i in n:
        res=True
        for j in a:
            if i==j:
                res=False
        if res:
            a.append(i)
    return a
n=input()
mylist=list(map(int,n.split()))

print(*unique(mylist))
        

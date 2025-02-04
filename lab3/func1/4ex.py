def prime_check(list):
    a=[]
    for x in list:
        res=True
        if x==0 or x==1 or x<0:
            continue
        for i in range(2,x//2+1,1):
            if x%i==0:
                res=False
                break
        if(res):
            a.append(x)

    
    return a

n=input()
mylist=list(map(int,n.split()))

print(*prime_check(mylist))

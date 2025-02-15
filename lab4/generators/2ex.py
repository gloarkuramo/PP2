def even(n):
    a=[]
    for i in range(n):
        if i%2==0:
            a.append(i)
    return a
n=int(input())
for i in even(n):
    print(i,end=",")
    
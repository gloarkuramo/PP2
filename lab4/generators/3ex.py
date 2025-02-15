def di(n):
    a=[]
    for i in range(n):
        if i%12==0:
            a.append(i)
    return a
n=int(input())
print(*di(n))

def square(n):
    a=[]
    for i in range(n):
        a.append(i*i)
    return a
n=int(input())

print(*square(n))
a=list(map(int,input().split()))
s=1
for i in range(len(a)):
    s*=a[i]
print(s)
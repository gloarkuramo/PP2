a=input()
def reverse(a):
    b=a.split()
    s=[]
    for i in range(-1,-(len(b)+1),-1):
    
        s.append(b[i])
    return s
print(*reverse(a))


def palindrome(a):
    s=[]
    b=[]
    for i in a:
        s.append(i)
        b.append(i)
    s.reverse()

    if s==b:
        return True
    return False
a=str(input())
if(palindrome(a)):
    print("Yes")
else:
    print("Lol, No")


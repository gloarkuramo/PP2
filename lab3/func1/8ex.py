def spy_game(nums):
    a=[]
    for i in nums:
        if i==0 or i==7:
            a.append(i)
    for i in range(len(a)-2):
        if a[i]==0 and a[i+1]==0 and a[i+2]==7:
            return True
    return False
n=input()
mylist=list(map(int,n.split()))

if spy_game(mylist):
    print("Yes")
else:
    print("No")

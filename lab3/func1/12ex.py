def histogram(n):
    for i in n:
        print("*"*i, end="\n")
 
n=input("numbers:")
mylist=list(map(int,n.split()))
histogram(mylist)
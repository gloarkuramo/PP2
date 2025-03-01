n=input()
t=n[0]
for i in range(1,len(n)):
    if n[i]==n[i].capitalize():
        t=t+" "+n[i]
    else:
        t=t+n[i]
print(t)

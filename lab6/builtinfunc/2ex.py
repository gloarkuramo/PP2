a=input()
upper=0
lower=0
for i in a:
    if i>='A' and i<='Z':
        upper+=1
    else:
        lower+=1
print(upper)
print(lower)

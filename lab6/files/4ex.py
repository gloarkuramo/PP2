file=open("exp.txt","r")
a=[]
for i in file:
    a.append(i)

file.close()
print(len(a))
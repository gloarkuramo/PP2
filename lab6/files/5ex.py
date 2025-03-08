a=list(map(str, input(). split(" ")))

file=open("exp.txt","w")
t=""
for i in a:
    file.write(i)
    file.write("\n")

file.close()
from Dictionary import movies
def filter(a):
    res=[]
    for i in movies:
        if i["category"]==a:
            res.append(i["name"])
    return res
c=input()
print(*filter(c))

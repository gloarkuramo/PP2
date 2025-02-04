from Dictionary import movies
def filter(a):
    res=[]
    for i in a:
        if i["imdb"]>5.5:
            res.append(i)
    return res
print(filter(movies))

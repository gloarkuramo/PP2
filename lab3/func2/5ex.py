from Dictionary import movies
def filter(a):
    s=0
    for i in movies:
        if i["category"]==a:
            s+=i["imdb"]
    return s/len(movies)
name=input()
print(filter(name))


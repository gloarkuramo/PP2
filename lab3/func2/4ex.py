from Dictionary import movies
def average(a):
    s=0
    for i in a:
        s+=i["imdb"]
    return s/len(a)
print(average(movies))



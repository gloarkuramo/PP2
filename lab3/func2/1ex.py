from Dictionary import movies
def filter(a):
    if a["imdb"]>5.5:
        return True
    return False
print(f"chose a number from {len(movies)} to 0 to select the movie, and we will check is it higher than 5.5")
a=int(input())
if(filter(movies[a])):
    print("It is higher")
else:
    print("No it is not higher")
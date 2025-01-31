#dictionaries

#syntex (ordered) 
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("\n")
print(car)
print("\n")
print(car["brand"])
print("\n")



x = car.keys()
#adding new key and declaring value at the moment

print(x) #before the change
car["color"] = "white"
print(x) #after the change


print("\n")
#Remwoing and updating
car.update({"color": "red"})
print(car)
car.pop("model")
print(car)


#nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("\n")
#how to access
print(myfamily["child2"]["name"])
#sets

#can store any value
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
thisset.add("orange")
print(thisset)

#adding set values 
thisset.add("orange")
print(thisset)


#adding two sets 
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


print("\n")
#deleting set values
thisset.discard("banana")
print(thisset)


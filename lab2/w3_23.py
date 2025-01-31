#lists


#syntex and accessing by "if" statement
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#range
print(thislist[:-2])
print(thislist[2:5])

#changing the value
thislist[1] = "blackcurrant"
print(thislist)

#adding elements
thislist.append("watermelon")
print(thislist)

#removing elements 
t = ["apple", "banana", "cherry"]
t.pop(1)
print(t)
t.clear()
print(t)

#lsit comprihension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#reversing
fruits.sort(reverse=True)
print(fruits)
#tuples

#Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print("\n")
#tuple length
t_tuple = ("apple", "banana", "cherry")
print(len(t_tuple))



print("\n")
#Changing tuple values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



print("\n")
#unpacking tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


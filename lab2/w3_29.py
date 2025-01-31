#for

for x in "banana":
  print(x)

#using break statement
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")



print("\n")
#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
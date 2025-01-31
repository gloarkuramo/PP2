#booleans


#following returns True value
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print("\n")

#following returns True value
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
print("\n")

print(10 > 9)
print(10 == 9)
print(10 < 9)

#we can use it in functions
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
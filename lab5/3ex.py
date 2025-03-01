import re

n=input()

condition=r"\b[a-z]+_[a-z]+\b"
x=re.findall(condition,n)

print(x)
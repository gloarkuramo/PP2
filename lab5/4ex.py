import re

n=input()

condition=r"\b[A-Z][a-z]+\b"

x=re.findall(condition,n)

print(x)

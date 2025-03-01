import re

n=input()

prompt=r"[ .,]"

x=re.sub(prompt,":",n)
print(x)

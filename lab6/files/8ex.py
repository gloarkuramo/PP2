import os
import string

alphabet = list(string.ascii_uppercase)

for i in alphabet:
    path=f"{i}.txt"
    if os.path.exists(path):
        os.remove(path)
    else:
        print("nope")

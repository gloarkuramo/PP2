import os 

path=os.path.abspath("exp.txt")

if os.path.exists(path):
    print(path)
    print(os.path.dirname(path))
else:
    print("File not exist")
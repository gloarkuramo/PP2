import os

path="test"

def check():
    print("Status of existence: ",end=" ")
    if os.path.exists(path):
        print("Exist")
    else:
        print("Not exist")
        return 0

    print("Status of readibility: ",end=" ")
    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Non-readable")

    print("Status of writeability: ",end=" ")
    if os.access(path, os.W_OK):
        print("writeable")
    else:
        print("Non-writeable")

    print("Status of executability: ",end=" ")

    if os.access(path, os.X_OK):
        print("executable")
    else:
        print("Non-executable")

check()
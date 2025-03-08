import string

alphabet = list(string.ascii_uppercase)
for i in alphabet:
    file=open(f"{i}.txt","w")
    file.write(i)
    file.close()

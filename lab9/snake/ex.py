f=open('best.txt','w+')

a =int(input())
score = 5
score+=a

f.write(str(score))
f.seek(0)
print(f.readline())

f.close()
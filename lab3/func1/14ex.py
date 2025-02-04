from random import randint
def game(n):
    print("Take a guess!")
    t=int(input())
    if(t==main):
        print(f"Good job! You guessed my number in {n} guesses!")
        return True
    elif t>main:
        print("Your guess is too high.")
        
    elif t<main:
        print("Your guess is too low.")
    return False
main=randint(1,20)
s=1
while(True):
    if(game(s)):
        print("Do you want continue? yes/no")
        a=input()
        if(a=="no"):
            print("ok, goodbye")
            break
        s=1
        main=randint(1,20)
    else:
        s+=1

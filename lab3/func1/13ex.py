from random import randint
def game(n):
    print("Take a guess!")
    t=int(input())
    if(t==main):
        print(f"Good job, {a}! You guessed my number in {n} guesses!")
        return False
    elif t>main:
        print("Your guess is too high.")
        
    elif t<main:
        print("Your guess is too low.")
    return True
        

print("Hello! What is your name?")
a=input()
print(f"Well, {a}, I am thinking of a number between 1 and 20.")
main=randint(1,20)

s=1
while(game(s)):
    s+=1
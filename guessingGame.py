import random

print("number guessing game")

number=random.randint(1,9)
chances=0

while chances <5:
    guess=int(input("enter your guess from 1-9"))
    guess==number
    if guess==number:
        print("congrats!! you win")
        break
    elif guess<number:
        print("sorry, you didnt get it right")
    else:
        print("sorry, you guessed too high number")
    chances+=1
if not chances < 5:
    print("you lost :(. the number is:-", number)
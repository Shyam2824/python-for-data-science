import random

jackpots= random.randint(1,100)

guess=int(input("Guess your number: "))
counter=1

while guess!= jackpots:
    if guess < jackpots:
        print("Wrong 👎! Guess higher")
        
    else:
        print("Wrong 👎! Guess lower")
        
    guess=int(input("Guess your number: "))
    counter +=1

else:
    print("correct 👍 your guess")
    print("your attempts : " , counter)
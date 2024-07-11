import random

gameOver=False

userAttempts=0

correctGuess=random.randint(1,100)

while userAttempts<=10:
    userGuess=int(input("Enter a Number 1-100: "))
    while userGuess<1 or userGuess>100:
        print("Please enter a number under between 1 and 100")
        userGuess=int(input("Enter a Number 1-100: "))
    if userGuess>=1 or userGuess<=100:
        userAttempts+=1
        if userGuess==correctGuess:
            print(f"You win! The number was {correctGuess}!")
            break
        if userGuess>correctGuess:
            print("Too High! Try again")
        if userGuess<correctGuess:
            print("Too Low! Try again")

if userAttempts>=10:
    print("You ran out of guesses!")
import random

wordList = [
    "house", "earth", "smile", "bread", "angel", "tiger", "cloud", "queen", 
    "grape", "plant", "river", "music", "chair", "horse", "paper", "beach", 
    "lemon", "onion", "south", "light", "sword", "storm", "watch", "chess", 
    "dance"
]

word = random.choice(wordList)

word = word.lower()

attempts = 0

max_attempts = 6

while attempts < max_attempts:
    guess = input("Enter a 5-letter word: ").lower()

    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        continue

    feedback = [''] * 5

    for i, letter in enumerate(guess):
        if letter == word[i]:
            feedback[i] = f"{letter}*"
        elif letter in word:
            feedback[i] = letter.upper()
        else:
            feedback[i] = letter

    print("Feedback:", " ".join(feedback))

    if guess == word:
        print(f"You win! The word was '{word}'.")
        break

    attempts += 1

if attempts == max_attempts:
    print(f"Game over! The word was '{word}'.")

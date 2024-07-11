word = "fires"
guesses = 0

def check_word(guess):
    for j in range(len(word)):
        if j < len(guess) and guess[j] == word[j]:
            print(f"{guess[j]} is in the word and in the correct position.")
        elif guess[j] in word:
            print(f"{guess[j]} is in the word but not in the correct position.")
        else:
            print(f"{guess[j]} is not in the word.")

correct_guess = False

while guesses < 6:
    guess = input("Enter a Word: ")
    
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        continue
    
    guesses += 1
    
    if guess == word:
        print("You win!")
        correct_guess = True
        break
    
    check_word(guess)

if not correct_guess:
    print(f"Sorry, you didn't guess the word. The correct word was '{word}'.")
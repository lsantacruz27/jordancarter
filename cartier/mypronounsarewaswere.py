word = "the chairs are not race cars"
wordList = []
lives = 11

for i in word:
    if i != " ":
        wordList.append("_")
    else:
        wordList.append(" ")

tempWord = "".join(wordList)

while lives >= 0:
    guess = input("Enter a letter: ")

    found = False
    for i in range(len(word)):
        if word[i] == guess:
            wordList[i] = guess
            found = True

    tempWord = "".join(wordList)
    print(tempWord)

    if "_" not in wordList:
        print("Congratulations! You guessed the word correctly.")
        break

    if not found:
        lives = lives-1
        print(f"Wrong guess! You have {lives} lives left.")

if lives <=0:
    print("Sorry, you're out of lives. The word was:", word)

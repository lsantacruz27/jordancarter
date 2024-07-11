import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


userCash = 3000
gameOver = False

def winCheck():
    global userCash
    if dealerValue > 21:
        print("The dealer busted")
        userCash += userBet * 2

    elif userValue > dealerValue:
        print("You win!")
        userCash += userBet * 2

    elif userValue < dealerValue:
        print("You lose.")

    elif userValue== dealerValue:
        print("Push!")
        userCash += userBet

def printTable(firstCard):
    global userHand, dealerHand, userCash, userValue, dealerValue
    
    userValue = sum(userHand)
    dealerValue = sum(dealerHand)
    
    userHandStr = [card if card != 11 else 'A' for card in userHand]
    dealerHandStr = [card if card != 11 else 'A' for card in dealerHand]

    if 11 in userHand and userValue > 21:
        userValue -= 10

    if 11 in dealerHand and dealerValue > 21:
        dealerValue -= 10

    print(f"You have ${userCash}\n")
    print(f"Dealer's hand (?):\n{firstCard}, {dealerHandStr[1:]}\n")
    print(f"Your hand({userValue}):\n{userHandStr}\n")



def newHand():
    global userHand, dealerHand
    userHand = [random.choice(deck) for i in range(2)]
    dealerHand = [random.choice(deck) for i in range(2)]

while gameOver == False:
    userHand = []
    dealerHand = []
    userBet = int(input(f"Place your bets (You have ${userCash}): "))
    while userBet<0:
        print("Please enter a positive number.")
        userBet = int(input(f"Place your bets (You have ${userCash}): "))
    userCash -= userBet
    newHand()
    printTable("?")
    if userValue==21:
        print("Blackjack!")
        userCash=userBet+(userBet*1.5)
        continue
    hitStand = input("Would you like to hit or stand: ")

    if hitStand == "hit":
        while hitStand != "stand":
            userHand.append(random.choice(deck))
            printTable("?")
            userValue = sum(userHand)

            if userValue > 21:
                    printTable(dealerHand[0])
                    print("You busted")
                    break
            
            hitStand = input("Would you like to hit or stand: ")

    if hitStand == "stand":
       
        dealerValue = sum(dealerHand)

        while dealerValue < 17:
            dealerHand.append(random.choice(deck))
            dealerValue = sum(dealerHand)

        printTable(dealerHand[0])

        winCheck()
    
    if userCash <= 0:
        print("You're out of cash! Game over.")
        gameOver = True
    else:
        playAgain = input("Do you want to play again? (yes/no): ").lower()
        if playAgain != "yes":
            gameOver = True
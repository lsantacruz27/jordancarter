import random

cards=["a",2,3,4,5,6,7,8,9,10,10,10,10]
playerMoney=3000

playerCards=[]
dealCards=[]

def newCards():
    playerCards=[]
    dealCards=[]


def printTable():
    print("")
    print("Dealer's Cards:")
    print(f"?, {dealCards[1]}")
    print("")
    print("Your Cards:")
    print(playerCards)
    print("Your Money:")

def printEndTable():
    print("")
    print("Dealer's Cards:")
    print(dealCards)
    print("")
    print("Your Cards:")
    print(playerCards)
    print("Your Money:")

while True:
    print(f"You have {playerMoney}.")
    playerBet=int(input("Place Your Bets: "))
    playerMoney-=playerBet
    playerCards=[]
    dealCards=[]
    for i in range(2):
        dealCards.append(random.choice(cards))
    for i in range(2):
        playerCards.append(random.choice(cards))
    playerHits=[""]
    printTable()
    playerChoice=input("Would you like to hit or stand: ")
    while playerChoice!="stand":
        playerChoice=input("Would you like to hit or stand: ")
        if playerChoice=="hit":
            playerCards.append(random.choice(cards))
            printTable()
            for i in range(len(dealCards)): 
                if i == "a":
                    i = 11
            playerVal=int(sum(playerCards))
            if playerVal>21:
                print("You busted all over the table. Your friends at the table stare at you in shock. The dealer looks weirdly excited. You look back at your cards in shame. Your friends all gather around looking shocked yet their mouths on thier faces start to smile")
            break
    if playerChoice=="stand":
        printTable()
        for i in range(len(dealCards)): 
            if i == "a":
                i = 11
        dealVal=int(sum(dealCards))
        if dealVal>int(sum(playerCards)):
            printEndTable()
            print("Dealer wins.")
            continue
        for i in range(len(dealCards)): 
            if i == "a":
                i = 11
        if int(sum(dealCards))<int(sum(playerCards)):
            printEndTable()
            print("You win!")
            playerMoney+=playerBet*2
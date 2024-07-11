gameBoard=[
    ["#","#","#","#","#","#","#","#"],
    ["#","#","-","-","-","-","#","#"],
    ["#","-","&","-","B","-","#","#"],
    ["#","#","#","-","-","-","#","#"],
    ["#","E","#","#","*","-","#","#"],
    ["#","-","#","-","-","-","#","#"],
    ["#","-","*","-","-","*","-","#"],
    ["#","-","-","-","-","-","-","#"],
    ["#","#","#","#","#","#","#","#"]
]
coins=0
gameWin=False

def printBoard():
    print(coins)
    for row in gameBoard:
        print(row)


printBoard()

rowCoord=2
columnCoord=2

while gameWin==False:
    userMove=input("Use WASD to move: ")

    if userMove=="w" and gameBoard[rowCoord-1][columnCoord]=="E":
        printBoard()
        print("You win!")
        gameWin=True
    elif userMove=="s" and gameBoard[rowCoord+1][columnCoord]=="E":
        print("You win!")
        printBoard()
        gameWin=True
    elif userMove=="a" and gameBoard[rowCoord][columnCoord-1]=="E":
        printBoard()
        print("You win!")
        gameWin=True
    elif userMove=="d" and gameBoard[rowCoord][columnCoord+1]=="E":
        printBoard()
        print("You win!")
        game=True

    elif userMove=="w" and gameBoard[rowCoord-1][columnCoord]=="*":
        coins+=1
        printBoard()
        print("You got a coin!")
    elif userMove=="s" and gameBoard[rowCoord+1][columnCoord]=="*":
        print("You got a coin!")
        coins+=1
        printBoard()
    elif userMove=="a" and gameBoard[rowCoord][columnCoord-1]=="*":
        coins+=1
        printBoard()
        print("You got a coin!")
    elif userMove=="d" and gameBoard[rowCoord][columnCoord+1]=="*":
        coins+=1
        printBoard()
        print("You got a coin!")

    elif userMove=="w" and gameBoard[rowCoord-1][columnCoord]=="B":
        if userMove=="w" and gameBoard[rowCoord-2][columnCoord]=="#":
            printBoard()
            print("You hit a wall, choose a different direction")
        elif userMove=="w" and gameBoard[rowCoord-2][columnCoord]=="-" or gameBoard[rowCoord-2][columnCoord]=="*":
            rowCoord -= 1
            gameBoard[rowCoord][columnCoord]="&"
            gameBoard[rowCoord+1][columnCoord]="-"
            gameBoard[rowCoord-1][columnCoord]="B"
            printBoard()
        if userMove=="w" and gameBoard[rowCoord-1][columnCoord]=="*":
            coins+=1
            printBoard()
            print("You got a coin!")
        
    elif userMove=="s" and gameBoard[rowCoord+1][columnCoord]=="B":
        if userMove=="s" and gameBoard[rowCoord+2][columnCoord]=="#":
            printBoard()
            print("You hit a wall, choose a different direction")
        elif userMove=="s" and gameBoard[rowCoord+2][columnCoord]=="-" or gameBoard[rowCoord+2][columnCoord]=="*":
            rowCoord += 1
            gameBoard[rowCoord][columnCoord]="&"
            gameBoard[rowCoord-1][columnCoord]="-"
            gameBoard[rowCoord+1][columnCoord]="B"
            printBoard()
        if userMove=="s" and gameBoard[rowCoord+1][columnCoord]=="*":
            coins+=1
            printBoard()
            print("You got a coin!")
    elif userMove=="a" and gameBoard[rowCoord][columnCoord-1]=="B":
        if userMove=="a" and gameBoard[rowCoord][columnCoord-2]=="#":
            printBoard()
            print("You hit a wall, choose a different direction")
        elif userMove=="a" and gameBoard[rowCoord][columnCoord-2]=="-" or gameBoard[rowCoord][columnCoord-2]=="*":
            columnCoord -= 1
            gameBoard[rowCoord][columnCoord]="&"
            gameBoard[rowCoord][columnCoord+1]="-"
            gameBoard[rowCoord][columnCoord-1]="B"
            printBoard()
        if userMove=="a" and gameBoard[rowCoord][columnCoord-1]=="*":
            coins+=1
            printBoard()
            print("You got a coin!")
    elif userMove=="d" and gameBoard[rowCoord][columnCoord+1]=="B":
        if userMove=="d" and gameBoard[rowCoord][columnCoord+2]=="#":
            printBoard()
            print("You hit a wall, choose a different direction")
        elif userMove=="d" and gameBoard[rowCoord][columnCoord+2]=="-" or gameBoard[rowCoord][columnCoord+2]=="*":
            columnCoord += 1
            gameBoard[rowCoord][columnCoord]="&"
            gameBoard[rowCoord][columnCoord-1]="-"
            gameBoard[rowCoord][columnCoord+1]="B"
            printBoard()
        if userMove=="d" and gameBoard[rowCoord][columnCoord+1]=="*":
            coins+=1
            printBoard()
            print("You got a coin!")

    elif userMove=="w" and gameBoard[rowCoord-1][columnCoord]=="#":
        printBoard()
        print("You hit a wall, choose a different direction")
    elif userMove=="w" and gameBoard[rowCoord-1][columnCoord]=="-" or gameBoard[rowCoord-1][columnCoord]=="*":
        rowCoord -= 1
        gameBoard[rowCoord][columnCoord]="&"
        gameBoard[rowCoord+1][columnCoord]="-"
        printBoard()
    elif userMove=="s" and gameBoard[rowCoord+1][columnCoord]=="#":
        print("You hit a wall, choose a different direction")
        printBoard()
    elif userMove=="s" and gameBoard[rowCoord+1][columnCoord]=="-" or gameBoard[rowCoord+1][columnCoord]=="*":
        rowCoord += 1
        gameBoard[rowCoord][columnCoord]="&"
        gameBoard[rowCoord-1][columnCoord]="-"
        printBoard()
    elif userMove=="a" and gameBoard[rowCoord][columnCoord-1]=="#":
        printBoard()
        print("You hit a wall, choose a different direction")
    elif userMove=="a"and gameBoard[rowCoord][columnCoord-1]=="-" or gameBoard[rowCoord][columnCoord-1]=="*":
        columnCoord -= 1
        gameBoard[rowCoord][columnCoord]="&"
        gameBoard[rowCoord][columnCoord+1]="-"
        printBoard()
    elif userMove=="d" and gameBoard[rowCoord][columnCoord+1]=="#":
        printBoard()
        print("You hit a wall, choose a different direction")
    elif userMove=="d" and gameBoard[rowCoord][columnCoord+1]=="-" or gameBoard[rowCoord][columnCoord+1]=="*":
        columnCoord += 1
        gameBoard[rowCoord][columnCoord]="&"
        gameBoard[rowCoord][columnCoord-1]="-"
        printBoard()

    elif userMove!="w" or userMove!="a" or userMove!="s" or userMove!="d":
        printBoard()
        print("Please enter only w, a, s, or d.")
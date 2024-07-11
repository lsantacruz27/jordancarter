board=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
def print_board():
    for row in board:
        print(row)

gameover=False

while gameover==False:

    selection=input("Player 1, enter a column and a row: ")
    if board[row][column]==1 or 2:
        print("Please choose an empty space")
        row=int(selection[0])
        column=int(selection[1])
    else:
        board[row][column]=1
    print_board()

    selection=input("Player 2, enter a column and a row: ")
    if board[row][column]==1 or 2:
        print("Please choose an empty space")
        row=int(selection[0])
        column=int(selection[1])
    else:
        board[row][column]=2
    print_board()
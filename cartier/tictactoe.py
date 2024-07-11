board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def print_board():
    for row in board:
        print(row)

def check_winner():
    for row in board:
        if all([cell == row[0] and cell != 0 for cell in row]):
            return row[0]

    for col in range(3):
        if all([board[row][col] == board[0][col] and board[row][col] != 0 for row in range(3)]):
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0

game_over = False
current_player = 1

while not game_over:
    print_board()
    selection = input(f"Player {current_player}, enter a row and a column (e.g., '<row> <column>'): ")
    try:
        row, column = map(int, selection.split())
    except ValueError:
        print("Invalid input format. Please enter two numbers separated by a space.")
        continue
    
    if not (0 <= row < 3 and 0 <= column < 3):
        print("Invalid row or column. Please enter numbers between 0 and 2.")
        continue
    
    if board[row][column] != 0:
        print("That space is already taken. Please choose an empty space.")
        continue
    
    board[row][column] = current_player

    winner = check_winner()
    if winner != 0:
        print_board()
        print(f"Player {winner} wins!")
        game_over = True
    elif all([cell != 0 for row in board for cell in row]):
        print_board()
        print("It's a tie!")
        game_over = True

    current_player = 2 if current_player == 1 else 1

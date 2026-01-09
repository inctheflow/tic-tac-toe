board = [" "] * 9

# function to print the current stat of the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")



# Function to handle  player move
#function for player move with input validation and checking for occupied positions
def player_move(player):
    while True:
        move = input(f"Player {player}, choose your position (0-8): ")

        if not move.isdigit():
            print("Please enter a number(0-8)")
            continue

        move = int(move)

        if move < 0 or move > 8:
            print("Position must be between 0 and 8.")
            continue

        if board[move] != " ":
            print("Position is already taken: Choose another Position.")
            continue
            
        board[move] = player
        break

#fucntion to check winner
def check_winner(player):
    win_combinations = {
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    }
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
        else:
            return False

#function to check for draw
def check_draw():
    return " " not in board

# Game loop which alternates player
current_player = "X"
while True:
    print_board()
    player_move(current_player)

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


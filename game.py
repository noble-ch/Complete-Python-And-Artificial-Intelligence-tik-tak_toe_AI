# Tic-tac-toe board
board = [' '] * 9

# Players
player1 = 'X'
player2 = 'O'

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function for a player to make a move
def make_move(player):
    while True:
        move = int(input(f"Player {player}, enter your move (0-8): "))
        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = player
        break

# Main game loop
def play_game():
    print("Let's play Tic-Tac-Toe!")
    print_board()

    while True:
        if check_winner(board, player1):
            print("Player X wins!")
            break
        elif check_winner(board, player2):
            print("Player O wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        make_move(player1)
        print_board()

        if check_winner(board, player1):
            print("Player X wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        make_move(player2)
        print_board()

# Start the game
play_game()

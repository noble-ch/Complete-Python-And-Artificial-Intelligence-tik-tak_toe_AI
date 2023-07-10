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
    if player == player1:
        while True:
            move = int(input(f"Player {player}, enter your move (0-8): "))
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
            board[move] = player
            break
    else:
        print("AI's turn:")
        ai_move()

# Function for the AI to make a move


def ai_move():
    best_score = float('-inf')
    best_move = None

    # Check all available moves
    for i in range(9):
        if board[i] == ' ':
            board[i] = player2
            score = minimax(board, 0, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = player2

# Minimax algorithm


def minimax(board, depth, is_maximizing):
    scores = {
        player1: -1,
        player2: 1,
        'tie': 0
    }

    if check_winner(board, player1):
        return scores[player1]
    elif check_winner(board, player2):
        return scores[player2]
    elif is_board_full(board):
        return scores['tie']

    if is_maximizing:
        best_score = float('-inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = player2
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)

        return best_score
    else:
        best_score = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = player1
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)

        return best_score

# Main game loop


def play_game():
    print("Let's play Tic-Tac-Toe!")
    print_board()

    game_mode = input(
        "Select game mode (1 for Single Player, 2 for Multiplayer): ")
    while game_mode not in ['1', '2']:
        game_mode = input(
            "Invalid input. Select game mode (1 for Single Player, 2 for Multiplayer): ")

    current_player = player1  # Initialize the current player

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

        make_move(current_player)
        print_board()

        if game_mode == '1':
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

        else:
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1


# Start the game
play_game()

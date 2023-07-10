import tkinter as tk
from tkinter import messagebox

# Tic-tac-toe game logic encapsulated in a class


class TicTacToeGame:
    def __init__(self):
        # Tic-tac-toe board
        self.board = [' '] * 9

        # Players
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1

    # Function to check if a player has won
    def check_winner(self, player):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True

        return False

    # Function to check if the board is full
    def is_board_full(self):
        return ' ' not in self.board

    # Function for a player to make a move
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.update_board()

            if self.check_winner(self.current_player):
                messagebox.showinfo(
                    "Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1
                if self.current_player == self.player2 and self.game_mode == "Single Player":
                    self.ai_make_move()

    # Function for the AI to make a move
    def ai_make_move(self):
        best_score = float('-inf')
        best_move = None

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.player2
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '

                if score > best_score:
                    best_score = score
                    best_move = i

        self.make_move(best_move)

    # Minimax algorithm
    def minimax(self, board, depth, is_maximizing):
        scores = {
            self.player1: -1,
            self.player2: 1,
            'tie': 0
        }

        if self.check_winner(self.player1):
            return scores[self.player1]
        elif self.check_winner(self.player2):
            return scores[self.player2]
        elif self.is_board_full():
            return scores['tie']

        if is_maximizing:
            best_score = float('-inf')

            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.player2
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    best_score = max(score, best_score)

            return best_score
        else:
            best_score = float('inf')

            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.player1
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    best_score = min(score, best_score)

            return best_score

    # Function to reset the board
    def reset_board(self):
        self.board = [' '] * 9
        self.current_player = self.player1
        self.update_board()

    # Function to update the board GUI
    def update_board(self):
        for i, val in enumerate(self.board):
            buttons[i].config(text=val)


# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create the buttons for the board
buttons = []
for i in range(9):
    button = tk.Button(window, text=' ', font=('Arial', 24), width=6, height=3)
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Create the reset button
reset_button = tk.Button(window, text="Reset", font=('Arial', 16))
reset_button.grid(row=3, column=1, pady=10)

# Create the game instance
game = TicTacToeGame()

# Function to handle button clicks


def button_click(position):
    game.make_move(position)

# Function to handle reset button click


def reset_button_click():
    game.reset_board()


# Assign the button click functions
for i in range(9):
    buttons[i].config(command=lambda pos=i: button_click(pos))

# Assign the reset button click function
reset_button.config(command=reset_button_click)

# Function to handle game mode selection


def select_game_mode(mode):
    game.game_mode = mode


# Create the game mode selection buttons
single_player_button = tk.Button(window, text="Single Player", font=(
    'Arial', 16), command=lambda: select_game_mode("Single Player"))
single_player_button.grid(row=4, column=0, padx=10, pady=5)

multiplayer_button = tk.Button(window, text="Multiplayer", font=(
    'Arial', 16), command=lambda: select_game_mode("Multiplayer"))
multiplayer_button.grid(row=4, column=1, padx=10, pady=5)

# Run the GUI main loop
window.mainloop()

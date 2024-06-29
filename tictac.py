import numpy as np
import tkinter as tk
from tkinter import messagebox

# Initialize the board
def init_board():
    return np.full((3, 3), ' ')

# Check for a win
def check_win(board, player):
    for row in board:
        if np.all(row == player):
            return True
    for col in board.T:
        if np.all(col == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Check for a draw
def check_draw(board):
    return np.all(board != ' ')

# Make a move
def make_move(board, row, col, player):
    if board[row, col] == ' ':
        board[row, col] = player
        return True
    return False

# Minimax algorithm to find the best move
def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -np.inf
        for row in range(3):
            for col in range(3):
                if board[row, col] == ' ':
                    board[row, col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row, col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = np.inf
        for row in range(3):
            for col in range(3):
                if board[row, col] == ' ':
                    board[row, col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row, col] = ' '
                    best_score = min(score, best_score)
        return best_score

# Find the best move for the AI
def find_best_move(board):
    best_score = -np.inf
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row, col] == ' ':
                board[row, col] = 'O'
                score = minimax(board, 0, False)
                board[row, col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

# Update the board after a move
def update_board(buttons, board):
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=board[row, col], state='disabled' if board[row, col] != ' ' else 'normal')

# Handle button click
def button_click(row, col):
    if board[row, col] == ' ':
        board[row, col] = 'X'
        update_board(buttons, board)
        if check_win(board, 'X'):
            messagebox.showinfo("Tic-Tac-Toe", "Player X wins!")
            reset_board()
        elif check_draw(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
        else:
            ai_move = find_best_move(board)
            if ai_move:
                make_move(board, ai_move[0], ai_move[1], 'O')
                update_board(buttons, board)
                if check_win(board, 'O'):
                    messagebox.showinfo("Tic-Tac-Toe", "AI wins!")
                    reset_board()
                elif check_draw(board):
                    messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                    reset_board()

# Reset the board for a new game
def reset_board():
    global board
    board = init_board()
    update_board(buttons, board)

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

board = init_board()
buttons = []

# Add a frame for the buttons to improve layout
frame = tk.Frame(root, bd=3, relief='solid')
frame.pack(pady=10, padx=10)

for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(frame, text=' ', width=10, height=3, font=('Helvetica', 20), relief='solid', borderwidth=1,
                           command=lambda row=row, col=col: button_click(row, col))
        button.grid(row=row, column=col, padx=1, pady=1)  # Adding padding to create visible borders
        button_row.append(button)
    buttons.append(button_row)

# Add a reset button
reset_button = tk.Button(root, text="Reset", command=reset_board, font=('Helvetica', 14))
reset_button.pack(pady=10)

root.mainloop()

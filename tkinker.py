import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_mode = None # or "AI"

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            return True
        return False
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player =='X' else 'X'

    def check_winner(self, player):
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        return any(
            self.board[a] == self.board[b] == self.board[c] == player
            for a, b, c in win_combinations
        )
    
    def check_draw(self):
        return ' ' not in self.board
    
    def reset(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def computer_move(self):
        #try to win
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                if self.check_winner('O'):
                    return i
                self.board[i] = ' '

        #block 'X' win
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                if self.check_winner('X'):
                    self.board[i] = 'O'
                    return i
                self.board[i] = ' '

        #random move if there is no case of win/block
        available_moves = [i for i, v in enumerate(self.board) if v == ' ']
        return random.choice(available_moves)



#GUI
game = TicTacToe()
root = tk.Tk()
root.title("TIC TAC TOE by INCTHEFLOW")

mode_label = tk.Label(root, text = "Select Game Mode: ", font = ("Arial", 14))
mode_label.grid(row = 0, column = 0, columnspan = 3)

def set_human_mode():
    game.game_mode = "HUMAN"
    reset_gui()
    enable_board()

def set_ai_mode():
    game.game_mode = "AI"
    reset_gui()
    enable_board()

human_button = tk.Button(root, text = "Human vs Human", command = set_human_mode)
ai_button = tk.Button(root, text = "Human vs Computer", command = set_ai_mode)

human_button.grid(row = 1, column = 0, columnspan = 1)
ai_button.grid(row = 1, column = 2, columnspan = 1)


buttons = []

def disable_board():
    for button in buttons:
        button.config(state = "disabled")
def enable_board():
    for button in buttons:
        button.config(state = "normal")

disable_board()


def on_click(index):
    if game.game_mode is None:
        return #ignore clicks if mode is not selected
    
    player = game.current_player

    if not game.make_move(index):
        return

    #if game.make_move(index):
    buttons[index].config(text = game.board[index], state = "disabled")
    root.update_idletasks()

    if game.check_winner(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_gui()
            return
        
    if game.check_draw():
            messagebox.showinfo("Game Over It's a draw!")
            reset_gui()
            return

    game.switch_player()

    if game.game_mode == "AI" and game.current_player == 'O':
            ai_index = game.computer_move()
            game.make_move(ai_index)
            buttons[ai_index].config(text = "O", state = "disabled")
            root.update_idletasks()

            if game.check_winner('O'):
                messagebox.showinfo("Game Over", "Computer Wins!")
                reset_gui()
                return
        
            if game.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_gui()
                return
        
            game.switch_player()

def reset_gui():
    game.reset()
    for button in buttons:
        button.config(text = " ", state = "disabled")


for i in range(9):
    button = tk.Button(root, text = " ", width = 6, height = 4, font =("Arial", 20),
                    command = lambda i = i: on_click(i))
    button.grid(row = i//3 + 2, column = i%3)
    buttons.append(button)

root.mainloop()


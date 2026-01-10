import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

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
            self.board[a] == self.board[b] == self.board[c] == self.current_player
            for a, b, c in win_combinations
        )
    
    def check_draw(self):
        return ' ' not in self.board
    
    def reser(self):
        self.board = [' '] * 9
        self.current_player = 'X'



#GUI
game = TicTacToe()
root = tk.Tk()
root.title("TIC TAC TOE by INCTHEFLOW")

buttons = []

def on_click(index):
    player = game.current_player
    if game.make_move(index):
        buttons[index].config(text = game.board[index], state = "disabled")

        if game.check_winner(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_gui()
            return
        
        if game.check_draw():
            messagebox.showinfo("Game Over It's a draw!")
            reset_gui()
            return

        game.switch_player()

def reset_gui():
    game.reset()
    for button in buttons:
        button.config(text = " ", state = "normal")


for i in range(9):
    button = tk.Button(root, text = " ", width = 6, height = 4, font =("Arial", 20),
                    command = lambda i = i: on_click(i))
    button.grid(row = i//3, column = i%3)
    buttons.append(button)

root.mainloop()


import random

class TicTacToe:
   def computer_move(self):
       #1. computer going for win
       for i in range(9):
           if self.board[i] == ' ':
               self.board[i] = 'O'
               if self.check_winner('O'):
                   print(f"computer chose position {i}.\n")
                   return
               self.board[i] = ' '
        
        #2. computer blocking player win
       for i in range(9):
           if self.board[i] == ' ':
               self.board[i] = 'X'
               if self.check_winner('X'):
                   self.board[i] = 'O'
                   print(f"Computer chose position{i}.\n")
                   return
               self.board[i] = ' '
       
       
       # random move for computer
       available_moves = [i for i, spot in enumerate(self.board) if spot == ' ']
       move = random.choice(available_moves)
       self.board[move] = 'O'
       print(f"computer chose positon {move}")
   
   def choose_game_mode(self):
       while True:
           print("Choose Game Mode:")
           print("1. Human vs Human")
           print("2. Human vs Computer")
           mode = input("Enter 1 or 2: ")

           if mode == '1':
               self.game_mode = "HUMAN"
               break
           elif mode == '2':
               self.game_mode = 'AI'
               break
           else:
               print("Invalid choice. Try again.")
            

     

   def __init__(self):
      self.board = [' '] * 9
      self.current_player = 'X'
      self.score = {'X':0, 'O':0}
      self.game_mode = None #"Human" or "AI"
      
   def print_board(self):
        print()
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print()

   def board_reset(self):
        self.board = [' '] * 9
        self.current_player = 'X'

   def player_move(self):
     while True:
          move = input(f"Player {self.current_player}, enter your move (0-8): ")
          if not move.isdigit():
               print("Please enter a number (0-8).")
               continue
          move = int(move)

          if move < 0 or move > 8:
               print("Position must be between 0 and 8.")
               continue
          if self.board[move] != ' ':
               print("Position {move} is already taken, choose another position.")
               continue
          self.board[move] = self.current_player
          break
     
   def check_winner(self, player):
     win_combinations = [
          (0, 1, 2), (3, 4, 5), (6, 7, 8),
          (0, 3, 6), (1, 4, 7), (2, 5, 8),
          (0, 4, 8), (2, 4, 6)
     ]
     for a, b, c in win_combinations:
        if self.board[a] == self.board[b] == self.board[c] == player:
            return True
        
          
     return False

   def check_draw(self):
     return ' ' not in self.board

#game loop
   def play_game(self):
     self.board_reset()
     
     while True:
          self.print_board()
          #self.player_move()
          if self.game_mode == 'AI' and self.current_player == 'O':
              self.computer_move()
          else:
              self.player_move()

          if self.check_winner(self.current_player):
               self.print_board()
               print(f"Player {self.current_player} wins!")
               self.score[self.current_player] += 1
               break
          if self.check_draw():
               self.print_board()
               print("It's a draw!")
               break
          self.current_player = 'O' if self.current_player == 'X' else 'X'


   def print_score(self):
     print("Scores: \n")
     print(f'Score - Player X: {self.score["X"]}, Player O: {self.score["O"]}\n')

game = TicTacToe()
game.choose_game_mode()
while True:
     game.play_game()
     game.print_score()

     again = input("Do uou want to play again (Y?N): ").upper()
     if again != 'Y':
          print("Thanks for playing TIC TAC TOE by INCTHEFLOW :)")
          break



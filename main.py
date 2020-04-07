#  Steps that should be implemented:
# 1 create a 3*3 Board
# 2 display Board
# 3 Play Game
# 4 handle turn
# 5 Check Win
#    Check row
#    Check column
#    Check diagonals
# 6 Check tie
# 7 Flip player

from enum import Enum

# # # # # # #  Global Variables # # # # # # 

# A 3*3 Board
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# define an enum to determine current player
class player(Enum):
  X_player = 1,
  O_player = 2
  

# define a variable to determine the end of the game
game_still_going = True

# who won? or tie
winner = None

# Display the initial stage of board
def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#  Start the game
def play_game():

  #  first we should display the board
  display_board()

#  continue the game since game_still_going be false
  while game_still_going:
    # handle the movement of player
    handle_turn(player)

    # Check if the game has ended
    check_if_game_over()

    # Flip to other player
    flip_player()

  # The game has ended
  if winner == player.X_player:
    print('X won.')
  elif winner == player.O_player:
    print('O won.')
  else:
    print('Tie.')
    



# Handle a single turn of an arbitrary player
def  handle_turn(player):
  position = input("please select a position between 1-9: ")
  is_not_digit = True
  while is_not_digit:
    if (position.isdigit() and int(position) < 10 and int(position) > 0):
      position = int(position) - 1
      is_not_digit=False
    else:
      position = input("please enter a vali number between 1-9: ")

  board[position] = "X"
  display_board()


def check_if_game_over():

  check_for_winner()

  check_if_tie()

  return

def check_for_winner():
  #declare the global winner var
  global winner
  
  # check rows
  row_winner = check_rows()

  # check columns
  column_winner = check_columns()

  # check daigonals
  daigonals_winner = check_daigonals()

  # Get the winner
  if row_winner:
    winner = row_winner

  elif column_winner:
    winner = column_winner
  
  elif daigonals_winner:
    winner = daigonals_winner
  
  else:
    winner = None

  return  


# if there was a winner swith the value of game_still_going and return the winner player
def check_rows():
  #declare the global variable
  global game_still_going

  # check if all the values in a row are the same (but not -)
  row1 = board[0] == board[1] == board[2] != '-'
  row2 = board[3] == board[4] == board[5] != '-'
  row3 = board[6] == board[7] == board[8] != '-'
  
  # return the winner player
  if row1:
    game_still_going = False
    return player.X_player if board[0] == 'X' else player.O_player
  
  elif row2:
    game_still_going = False
    return player.X_player if board[3]=='X' else player.O_player

  elif row3:
    game_still_going = False
    return player.X_player if board[6]=='X' else player.O_player
  else:
    return None

# if there was a winner swith the value of game_still_going and return the winner player
def check_columns():
    #declare the global variable
  global game_still_going

  # check if all the values in a row are the same (but not -)
  column1 = board[0] == board[3] == board[4] != '-'
  column2 = board[1] == board[4] == board[7] != '-'
  column3 = board[2] == board[5] == board[8] != '-'
  
  # return the winner player
  if column1:
    game_still_going = False
    return player.X_player if board[0] == 'X' else player.O_player
  
  elif column2:
    game_still_going = False
    return player.X_player if board[1]=='X' else player.O_player

  elif column3:
    game_still_going = False
    return player.X_player if board[2]=='X' else player.O_player
  else:
    return None

# if there was a winner swith the value of game_still_going and return the winner player
def check_daigonals():
  #declare the global variable
  global game_still_going

  # check if all the values in a row are the same (but not -)
  daigonals1 = board[0] == board[4] == board[8] != '-'
  daigonals2 = board[2] == board[4] == board[6] != '-'

  # return the winner player
  if daigonals1:
    game_still_going = False
    return player.X_player if board[0] == 'X' else player.O_player
  
  elif daigonals2:
    game_still_going = False
    return player.X_player if board[1]=='X' else player.O_player
  else:
    return None  



def check_if_tie() :
  return

def  flip_player():

  return



play_game()



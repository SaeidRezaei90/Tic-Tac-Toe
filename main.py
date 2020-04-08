#  Steps that should be implemented:
# 1 create a 3*3 Board
# 2 display Board
# 3 start Playing Game
# 4 handle turn
# 5 Check Game is ended
#   5.1 Check Win
#       Check row
#       Check column
#       Check diagonals
#   5.2 Check tie
# 6 Flip player

#### hadle that a player can not replace in another one

from enum import Enum

# # # # # # #  Global Variables # # # # # #

# A 3*3 Board
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# define an enum to determine current player
class player(Enum):
    X_player = 1,
    O_player = 2,

#define a current player to determine who is turn
current_player = player.X_player

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
  
  # declare global variable
  global current_player

  # ask which player start the game (X or O)
  initial_player = input("Which player wants to start the game, X or O ? ")
  valid_initial_player = True
  while valid_initial_player:
    if (str(initial_player).lower() == 'x'):
      current_player = player.X_player
      valid_initial_player = False
    elif (str(initial_player).lower() == 'o'):
      current_player = player.O_player
      valid_initial_player = False

    else:
      initial_player = input("Please select a character between O and X only: ")

    # first we should display the board
  display_board()

  # continue the game since game_still_going be false
  while game_still_going:
      # handle the movement of player
      handle_turn(current_player)

      # Check if the game has ended
      check_if_game_over()

      # Flip to other player
      flip_player()

  # The game has ended
  print()
  if winner == player.X_player:
      print('X won, congratulation')
  elif winner == player.O_player:
      print('O won, congratulation')
  else:
      print('Tie.')


# Handle a single turn of an arbitrary player
def handle_turn(player):
    position = input("please select a position between 1-9: ")
    is_not_digit = True
    # Check if the entered number is valid or not
    while is_not_digit:
        if (position.isdigit() and int(position) < 10 and int(position) > 0):
            position = int(position) - 1
        else:
            position = input("please enter a valid number between 1-9: ")
            continue
        
        if(board[position] == '-'):
          # Check 'X' should be written or 'O'
          if(player == player.X_player):
            board[position] = "X"
          else:
            board[position] = "O"

          is_not_digit = False
        
        else:
         print()
         position = input("please enter a valid number between 1-9, note that the entered position should be empty '-'.")

    
    
    display_board()


def check_if_game_over():

    check_for_winner()

    check_if_tie()

    return


def check_for_winner():
  # check rows
  check_rows()

  # check columns
  check_columns()

  # check daigonals
  check_daigonals()

  return


# if there was a winner swith the value of game_still_going and return the winner player
def check_rows():
    #declare the global variable
    global game_still_going, winner

    # check if all the values in a row are the same (but not -)
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    # return the winner player
    if row1:
        game_still_going = False
        winner = player.X_player if board[0] == 'X' else player.O_player
        return winner

    elif row2:
        game_still_going = False
        winner = player.X_player if board[3] == 'X' else player.O_player
        return winner

    elif row3:
        game_still_going = False
        winner = player.X_player if board[6] == 'X' else player.O_player
        return winner

    else:
        return None


# if there was a winner swith the value of game_still_going and return the winner player
def check_columns():
    #declare the global variables
    global game_still_going, winner

    # check if all the values in a row are the same (but not -)
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'

    # return the winner player
    if column1:
        game_still_going = False
        winner = player.X_player if board[0] == 'X' else player.O_player
        return winner

    elif column2:
        game_still_going = False
        winner = player.X_player if board[1] == 'X' else player.O_player
        return winner

    elif column3:
        game_still_going = False
        winner = player.X_player if board[2] == 'X' else player.O_player
        return winner

    else:
        return None


# if there was a winner swith the value of game_still_going and return the winner player
def check_daigonals():
    #declare the global variables
    global game_still_going, winner

    # check if all the values in a row are the same (but not -)
    daigonals1 = board[0] == board[4] == board[8] != '-'
    daigonals2 = board[2] == board[4] == board[6] != '-'

    # return the winner player
    if daigonals1:
        game_still_going = False
        winner = player.X_player if board[0] == 'X' else player.O_player
        return winner

    elif daigonals2:
        game_still_going = False
        winner = player.X_player if board[2] == 'X' else player.O_player
        return winner
        
    else:
        return None


def check_if_tie():
  # Declare the global variables
  global game_still_going, winner

  if (board[0]!='-' and board[1]!='-' and board[2]!='-' and board[3]!='-' and board[4]!='-' and board[5]!='-' and board[6]!='-' and board[7]!='-' and board[8]!='-'):
    game_still_going = False
    #winner = None

  return


def flip_player():
  # declare globals variables
  global current_player

  # Flip the current player
  if (current_player == player.X_player):
    current_player = player.O_player
  else:
    current_player = player.X_player

    return


play_game()

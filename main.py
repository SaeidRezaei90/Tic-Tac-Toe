# Steps that should be implemented:
#1 Board
#2 display Board
#3 Play Game
#4 handle turn
#5 Check Win
#   Check row
#   Check column
#   Check diagonals
#6 Check tie
#7 Flip player

from enum import Enum

####### Global Variables######

#A 3*3 Board
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-',  ]

#define an enum to determine current player
class current_player(Enum):
  X_player = 1,
  O_player = 2
  

#define a variable to determine the end of the game
game_still_going = True

#who won? or tie
winner = None

#Display the initial stage of board
def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():

  #first we should display the board
  display_board()

#continue the game since game_still_going be false
  while game_still_going:
    #handle the movement of player
    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  #The game has ended
  if winner == current_player.X_player:
    print('X won.')
  elif winner == current_player.O_player:
    print('O won.')
  else:
    print('Tie.')
    



#
def  handle_turn(player):
  position = input("please select a position between 1-9: ")
  is_digit = True
  while is_digit:
    if (position.isdigit() and int(position) <= 9 and int(position) > 0):
      position = int(position) - 1
      is_digit=False
    else:
      position = input("please enter a vali number between 1-9: ")

  board[position] = "X"
  display_board()


def check_if_game_over():

  check_if_win()

  check_if_tie()

  return

def check_if_win():
  #check rows

  #check columns

  #check daigonals
  return


def check_if_tie() :
  return

def  flip_player():

  return



play_game()



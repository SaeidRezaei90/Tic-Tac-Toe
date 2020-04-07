from enum import Enum

####### Global Variables######

#A 3*3 Board
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-',  ]

#define an enum to determine current player
class current_player(Enum):
  first_player = 1,
  second_player = 2

#Display the initial stage of board
def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():

  #first we should display the board
  display_board()

  #handle the movement of player
  handle_turn(current_player)

  check_if_game_over()

  flip_player()


#
def  handle_turn(current_player):
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

  return

def  flip_player():

  return



play_game()


# Steps we should implements
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
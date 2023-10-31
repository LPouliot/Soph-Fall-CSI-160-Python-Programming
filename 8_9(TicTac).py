"""
Author: Lily
Class: CSI-160-01
Assignment: Week 5 Lab
Due Date: 10/26/23

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""

import replit
import time

# Constants in are named in all caps (PEP8 Standard)
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '
TIE_GAME = 'tie'
BOARD_SIZE = 3

current_player = PLAYER_X  # Player X goes first

# Builds an EMPTY board
board = [
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]


def print_board():
    # Clear the screen
    replit.clear()

    """Prints the board to the console"""
    print('    0   1   2')
    print('  -------------')
    for i, row in enumerate(board):
        print(i, end="")
        for square in row:
            print(' | ' + square, end="")
        print(' |')
        print('  -------------')


def is_empty(row, col):
    """
    params row, col: (int) The row and Column to Check
    return: (boolean) If the row is EMPTY
    """
    # To check if the specified row and column are an empty square

    if board[row][col] == " ": # the [][] were found in the notes taken for last week
        return True # True when it is an empty slot
    else:
        return False # False when it is not an empty slot


def move(player, row, col):
    """
    Makes a game move

    If a move is legal, moves the player to the row and col
    and returns True. If a move is illegal, no move is made
    and returns False. Hint: Should make use of is_empty()

    param player: Either PLAYER_X or PLAYER_O
    param row, col: (int) The row and Column to move to
    return: (boolean) Success of the move
    """
    # Checking to see if the move was legal or not
    # Found out that using or helps keep all the actions in one row
    if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != ' ':
        return False # if the move was illegal
    else:
    # I had help with this portion of the lab from Hanne in class
    # The imputed row/col from the user can be found here and sets the coordinates
        board[row][col] = player
        return True

def determine_winner():
    """Determine if there is a winner

    return: Returns None if there is no winner.
            Returns PLAYER_O or PLAYER_X if one of them won.
            Returns 'tie' if noone wins
    """
    # This part was helped by both Savannah and Hanne in class

    # Step 1: Check the horizontals looking for a winner. If so return winner.
    # using multiple == along with and, helps to avoid many if statements
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0] # As this player wins

    # Step 2: Check the verticals looking for a winner. If so return winner.
    for col in range(BOARD_SIZE):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col] # As this player wins

    # Step 3: Check the diagonals looking for a winner. If so return winner.
    # This is a bit harder, since the numbers are not going to be as simple. (I used a physical paper to write it out)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    # Step 4: Check to see if there are empty squares. If there are empty squares, return None
    #         because no one has won the game yet
    #         If there are no empty squares return TIE_GAME
    #         because we didn't find a winner and all moves are made
    for r in board:
        if EMPTY in r:
            return None # This works instead of using False

    return TIE_GAME

while True:
    print()
    print_board()
    print()
    print('It is', current_player, 'turn')
    row = int(input('What is the row (0-2)? '))
    col = int(input('What is the col (0-2)? '))

    # Make sure the move is legal, if so make the move
    if is_empty(row, col):
        move(current_player, row, col)
    else:
        print('That is not a legal move!')
        time.sleep(2)
        continue

    # Check if there is a winner
    winner = determine_winner()
    if winner in (PLAYER_O, PLAYER_X):
        print_board()
        print('Congratulations', winner, '!!! You won!')
        print('But you are all winners')
        break

    if winner == TIE_GAME:
        print_board()
        print("It's a tie!!!")
        break

        # Let the other player have a turn
    if current_player == PLAYER_O:
        current_player = PLAYER_X
    else:
        current_player = PLAYER_O

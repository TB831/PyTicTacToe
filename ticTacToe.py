# For using the same code in either Python 2 or 3
from __future__ import print_function
import random

from IPython.display import clear_output
def display_board(board):
    '''
    Function to display the board
    '''
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    '''
    Function defined to take player input
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O?').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    '''
    Function assigns marker to the board position
    '''
    board[position] = marker

def win_check(board,mark):
    '''
    Function to check for winner
    '''
    return (if board[7] == mark and board[8] == mark and board[9] == mark) or
        (if board[4] == mark and board[5] == mark and board[6] == mark) or
        (if board[1] == mark and board[2] == mark and board[3] == mark) or
        (if board[1] == mark and board[5] == mark and board[9] == mark) or
        (if board[3] == mark and board[5] == mark and board[7] == mark) or
        (if board[1] == mark and board[4] == mark and board[7] == mark) or
        (if board[2] == mark and board[5] == mark and board[8] == mark) or
        (if board[3] == mark and board[6] == mark and board[9] == mark)

def choose_first():
    '''
    Function to randomly decide which player goes first
    '''
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    '''
    Function to return whether space on board is available
    '''
    return board[position] == ' '

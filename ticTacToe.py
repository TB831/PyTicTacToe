# For using the same code in either Python 2 or 3
from __future__ import print_function

## Note: Python 2 users, use raw_input() to get player input. Python 3 users, use input()
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

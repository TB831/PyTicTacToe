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
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark))

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

def full_board_check(board):
    '''
    function to check if board is full
    '''
    for i in range(0,10):
        if space_check(board, i):
            return False
        return True

def player_choice(board):
    '''
    function that inputs players next position then check if it is free
    '''
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your: (1-9) ')
    return int(position)

def replay():
    return raw_input('Do you want to play again? enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

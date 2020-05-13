"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    xcount = 0
    ycount = 0
    for row in board:
        for cell in row:
            if(cell == "X"):
                xcount = xcount + 1 
            else:    
                ycount = ycount + 1
    if(xcount == ycount):
        return "X" 
    else:
        return "Y"


def actions(board):
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                action.add((i, j))
    return action


def result(board, action):
    board[action[0]][action[1]] = action[2]
    return board 


def winner(board):
    winplayer = None
    won = False
    if ((board[0][1] == board[0][2] == board[0][0])):
        winplayer = board[0][0]
    elif(board[1][0] == board[1][1] == board[1][2]):
        winplayer = board[1][0]
    elif(board[2][0] == board[2][1] == board[2][2]):
        winplayer = board[2][0]
    elif(board[0][2] == board[1][2] == board[2][2]):
        winplayer = board[2][2]
    elif(board[1][0] == board[1][1] == board[2][1]):
        winplayer = board[2][1]
    elif(board[0][0] == board[1][0] == board[2][0]):
        winplayer = board[2][0]
    elif(board[0][0] == board[1][1] == board[2][2]):
        winplayer = board[0][0]
    elif(board[2][0] == board[1][1] == board[0][2]):
        winplayer = board[2][0]
    return winplayer
        



def terminal(board):
    terminal_state = False
    for row in board:
       for cell in row:
           if cell == None:
               return False 

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == "X"):
        return 1
    elif(winner(board) == "Y"):
        return -1 
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
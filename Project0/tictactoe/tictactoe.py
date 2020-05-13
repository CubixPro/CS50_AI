"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
dp = {}
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


b = initial_state()
dp[str(b)] = (1, 1)

def player(board):
    xcount = 0
    ocount = 0
    for i in range(3): 
        for cell in range(3):
            if(board[i][cell] == "X"):
                xcount = xcount + 1 
            elif(board[i][cell] == O):    
                ocount = ocount + 1
    if(ocount == xcount):
        return X
    else: 
        return O


def actions(board):
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                action.add((i, j))
    return action


def result(board, action):
    curr = player(board)
    newboard = copy.deepcopy(board) 
    newboard[action[0]][action[1]] = curr 
    return newboard 


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
    if winner(board) == True:
        return True
    for row in range(3):
       for cell in range(3):
           if board[row][cell] == None:
               return False 

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(winner(board) == "X"):
        return 1
    elif(winner(board) == O):
        return -1 
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current = player(board)
    actionset = actions(board)

    maxaction = None
    if terminal(board):
        return utility(board)
    """
    else:
        if(player == "X"):
            max = -1
            
            for action in actionset:
                newboard = result(board, action, player)
                move  = minimax(newboard)
                if(move >= max):
                    maxaction = action
                    max = move
        if(player == "Y"):
            min = 1 
            
            for action in actionset:
                newboard = result(board, action, player)
                move  = minimax(newboard)
                if(move <= min):
                    maxaction = action
                    max = move
        
    return maxaction
    """
    if(dp.get(str(board)) != None):
        return dp[str(board)]
    if (player == "X"):
        maxvalue(board)
        return dp[str(board)]
    else:
        minvalue(board)
        return dp[str(board)]
         


def maxvalue(board):
    if terminal(board):
        return utility(board)
    maxval = -2
    maxaction = None
    for action in actions(board):
        newboard = result(board, action)
        val = minvalue(newboard)
        if (val > maxval):
            maxval = val
            maxaction = action
    dp[str(board)] = maxaction
    return maxval

def minvalue(board):
    if terminal(board):
        return utility(board)
    minval = 4
    minaction = None
    for action in actions(board):
        newboard = result(board, action)
        val = maxvalue(newboard)
        if(val < minval):
            minval = val
            minaction = action
    dp[str(board)] = minaction
    return minval

"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    """
    x_count =0
    o_count =0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    if x_count <= o_count:
        return X
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (i,j) = action
    if action not in actions(board):
        raise Exception("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = None
    players = [X,O]
    for i in range(2):
        if ((board[0][0] == board[0][1] == board[0][2] == players[i]) 
            or (board[1][0] == board[1][1] == board[1][2] == players[i]) 
            or (board[2][0] == board[2][1] == board[2][2] == players[i]) 
            or (board[0][0] == board[1][0] == board[2][0] == players[i]) 
            or (board[0][1] == board[1][1] == board[2][1] == players[i]) 
            or (board[0][2] == board[1][2] == board[2][2] == players[i]) 
            or (board[0][0] == board[1][1] == board[2][2] == players[i]) 
            or (board[0][2] == board[1][1] == board[2][0] == players[i])):
            win = players[i]
    return win


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            min_value_result = min_value(result(board, action))
            if min_value_result > v:
                v = min_value_result
                optimal_action = action
    else:
        v = math.inf
        for action in actions(board):
            max_value_result = max_value(result(board, action))
            if max_value_result < v:
                v = max_value_result
                optimal_action = action
    return optimal_action

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
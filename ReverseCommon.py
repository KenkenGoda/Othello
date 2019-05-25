#ReverseCommon.py
import copy

NONE = None
WHITE = False
BLACK = True

def get_score(board,color):
    score = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == color:
                score += 1
    return score

def get_remain(board):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] is None:
                count += 1
    return count

def has_right_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if j <= 5 and board[i][j+1] == enemy:
        for k in range(j+2,8):
            if board[i][k] == color:
                return True
            elif board[i][k] == NONE:
                break
    return False

def has_left_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if j >= 2 and board[i][j-1] == enemy:
        for k in range(j-2,-1,-1):
            if board[i][k] == color:
                return True
            elif board[i][k] == NONE:
                break
    return False

def has_upper_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if i >= 2 and board[i-1][j] == enemy:
        for k in range(i-2,-1,-1):
            if board[k][j] == color:
                return True
            elif board[k][j] == NONE:
                break
    return False

def has_lower_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if i <= 5 and board[i+1][j] == enemy:
        for k in range(i+2,8):
            if board[k][j] == color:
                return True
            elif board[k][j] == NONE:
                break
    return False

def has_right_upper_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if i >= 2 and j <= 5 and board[i-1][j+1] == enemy:
        k = 2
        while i - k >= 0 and j + k < 8:
            if board[i-k][j+k] == color:
                return True
            elif board[i-k][j+k] == NONE:
                break
            k += 1
    return False

def has_left_lower_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if j >= 2 and i <= 5 and board[i+1][j-1] == enemy:
        k = 2
        while i + k < 8 and j - k >= 0:
            if board[i+k][j-k] == color:
                return True
            elif board[i+k][j-k] == NONE:
                break
            k += 1
    return False

def has_left_upper_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if i >= 2 and j >= 2 and board[i-1][j-1] == enemy:
        k = 2
        while i - k >= 0 and j - k >= 0:
            if board[i-k][j-k] == color:
                return True
            elif board[i-k][j-k] == NONE:
                break
            k += 1
    return False

def has_right_lower_reversible_stone(board,i,j,color):
    enemy = not(bool(color))
    if i <= 5 and j <= 5 and board[i+1][j+1] == enemy:
        k = 2
        while i + k < 8 and j + k < 8:
            if board[i+k][j+k] == color:
                return True
            elif board[i+k][j+k] == NONE:
                break
            k += 1
    return False


def is_game_set(board):
    if len(get_puttable_points(board,WHITE)) == 0 and len(get_puttable_points(board,BLACK)) == 0:
        return True
    return False

def get_puttable_points(board,color):
    points = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != NONE:
                continue
            if has_right_reversible_stone(board,i,j,color) or has_left_reversible_stone(board,i,j,color):
                points.append([i,j])
                continue
            if has_upper_reversible_stone(board,i,j,color) or has_lower_reversible_stone(board,i,j,color):
                points.append([i,j])
                continue
            if has_right_upper_reversible_stone(board,i,j,color) or has_left_lower_reversible_stone(board,i,j,color):
                points.append([i,j])
                continue
            if has_left_upper_reversible_stone(board,i,j,color) or has_right_lower_reversible_stone(board,i,j,color):
                points.append([i,j])
                continue
    return points

def put_stone(board,color,i,j):
    new_board = copy.deepcopy(board)
    if has_right_reversible_stone(new_board,i,j,color):
        k = j + 1
        while new_board[i][k] != color:
            new_board[i][k] = color
            k += 1
    if has_left_reversible_stone(new_board,i,j,color):
        k = j - 1
        while new_board[i][k] != color:
            new_board[i][k] = color
            k -= 1
    if has_upper_reversible_stone(new_board,i,j,color):
        k = i - 1
        while new_board[k][j] != color:
            new_board[k][j] = color
            k -= 1
    if has_lower_reversible_stone(new_board,i,j,color):
        k = i + 1
        while new_board[k][j] != color:
            new_board[k][j] = color
            k += 1
    if has_right_lower_reversible_stone(new_board,i,j,color):
        k = 1
        while new_board[i+k][j+k] != color:
            new_board[i+k][j+k] = color
            k += 1
    if has_left_upper_reversible_stone(new_board,i,j,color):
        k = 1
        while new_board[i-k][j-k] != color:
            new_board[i-k][j-k] = color
            k += 1
    if has_right_upper_reversible_stone(new_board,i,j,color):
        k = 1
        while new_board[i-k][j+k] != color:
            new_board[i-k][j+k] = color
            k += 1
    if has_left_lower_reversible_stone(new_board,i,j,color):
        k = 1
        while new_board[i+k][j-k] != color:
            new_board[i+k][j-k] = color
            k += 1
    new_board[i][j] = color
    return new_board

def print_board(board):
    print('　０ １ ２ ３ ４ ５ ６ ７')
    for i in range(8):
        row = str(i) + '|'
        for j in range(8):
            if board[i][j] == NONE:
                row += '　'
            elif board[i][j] == WHITE:
                row += '⚪️'
            else:
                row += '⚫️'
            row += '|'
        print(row)
    print(' ')



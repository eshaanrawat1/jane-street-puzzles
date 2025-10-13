import random 
import die_agony as da

N = 6
GOAL = (0, N-1)


def get_cell_score(board, nr, nc, dice, move_num, old_score):
    top = dice[0]
    new_score = top * move_num + old_score

    board[nr][nc] = new_score


def create_board(r, c, move_num, dice):
    board = [[None] * N for _ in range(N)]
    board[N-1][0] = 0


    while (r, c) != GOAL:
        dirs = []
        if da.in_bounds(r-1, c):
            dirs.append((r-1, c, da.roll_up))
        if da.in_bounds(r, c+1):
            dirs.append((r, c+1, da.roll_right))
        
        nxt_dir = random.choice(dirs)
        old_score = board[r][c]

        nr, nc, func = nxt_dir
        dice = func(dice)

        r, c = nr, nc
        move_num += 1

        get_cell_score(board, nr, nc, dice, move_num, old_score)
    
    normalize(board)
    return board


def normalize(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] is None:
                board[i][j] = random.randint(-750, 750)


def stringify_board(board):
    res = []
    for row in board:
        str_row = '_'.join(str(x) for x in row)
        res.append(str_row)
    return '_'.join(res)


def print_board(board):
    for row in board:
        print(row)
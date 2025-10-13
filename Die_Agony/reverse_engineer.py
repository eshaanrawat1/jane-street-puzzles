import random 
import die_agony as da

N = 6
GOAL = (0, N-1)

board = [[None] * N for _ in range(N)]
board[N-1][0] = 0


def get_cell_score(nr, nc, dice, move_num, old_score):
    top = dice[0]
    new_score = top * move_num + old_score

    board[nr][nc] = new_score


def create_board(r, c, move_num, dice):
    path = []

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

        get_cell_score(nr, nc, dice, move_num, old_score)

        path.append((r, c))
    return path


def normalize():
    for i in range(N):
        for j in range(N):
            if board[i][j] is None:
                board[i][j] = random.randint(-750, 750)


def stringify_board():
    res = []
    for row in board:
        str_row = '_'.join(x for x in row)
        res.append(str_row)
    return '_'.join(res)


def print_board():
    for row in board:
        print(row)



if __name__ == "__main__":
    dice = (5, 16, -8, 20, 18, 1)
    path = create_board(5, 0, 1, dice)
    normalize()
    print_board()
    print(stringify_board())
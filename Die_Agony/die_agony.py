N = 6
GOAL = (0, N-1)

def in_bounds(r, c):
    return 0 <= r < N and 0 <= c < N



def roll_up(dice):
    top, bot, front, back, left, right = dice
    return (back, front, top, bot, left, right)

def roll_down(dice):
    top, bot, front, back, left, right = dice
    return (front, back, bot, top, left, right)

def roll_left(dice):
    top, bot, front, back, left, right = dice
    return (left, right, front, back, bot, top)

def roll_right(dice):
    top, bot, front, back, left, right = dice
    return (right, left, front, back, top, bot)



def get_score(target, old_score, move_num, dice):
    top, bot, front, back, left, right = dice

    if top == 0:
        if (target - old_score) % move_num != 0:
            return False, None, None
        new_top = (target - old_score) // move_num
        new_dice = (new_top, bot, front, back, left, right)
        return True, target, new_dice

    else:
        new_score = top * move_num + old_score
        return (False, None, None) if new_score != target else (True, target, dice)



def dfs(board, r, c, score, move_num, dice, path):
    if (r, c) == GOAL:
        return True, path + [(r, c)]
    
    res, solve_path = False, None
    for nr, nc, func in [(r-1, c, roll_up), (r+1, c, roll_down), (r, c+1, roll_right), (r, c-1, roll_left)]:
        if not in_bounds(nr, nc):
            continue

        target = board[nr][nc]
        possible, new_score, new_dice = get_score(target, score, move_num, func(dice))

        if possible:
            res, solve_path = dfs(board, nr, nc, new_score, move_num+1, new_dice, path + [(r, c)])
            if res:
                return res, solve_path
    
    return (res, solve_path)


def main():
    board = [
        [57, 33, 132, 268, 492, 732],
        [81, 123, 240, 443, 353, 508],
        [186, 42, 195, 704, 452, 228],
        [-7, 2, 357, 452, 317, 395],
        [5, 23, -4, 592, 445, 620],
        [0, 77, 32, 403, 337, 452]
    ]

    result, path = dfs(board, 5, 0, 0, 1, (0, 0, 0, 0, 0, 0), [])
    path_set = {x for x in path}
    print(result, path)


    unvis_score = 0
    for i in range(N):
        for j in range(N):
            if (i, j) not in path_set:
                unvis_score += board[i][j]
    return unvis_score


def solve(board):
    _, path = dfs(board, 5, 0, 0, 1, (0, 0, 0, 0, 0, 0), [])
    return path


if __name__ == '__main__':
    print(main())
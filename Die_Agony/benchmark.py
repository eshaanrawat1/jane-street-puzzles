import time

import reverse_engineer as rev_e
import die_agony as da

def benchmark_solver(board):
    start = time.time()
    
    path = da.solve(board)
    end = time.time()
    duration = end - start

    return {
        "board_hash": rev_e.stringify_board(board),
        "solve_time": duration,
        "num_moves": len(path) if path else 0, 
    }
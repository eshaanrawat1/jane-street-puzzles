import time
import random
import sqlite3

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


def create_table():
    conn = sqlite3.connect('benchmarks.db')
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS board_benchmarks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        board_hash TEXT UNIQUE,
        solve_time REAL,
        num_moves INTEGER
    )
    ''')
    conn.commit()
    return cur, conn


def insert_benchmark(cur, conn, board_hash, solve_time, num_moves):
    try:
        cur.execute('''
        INSERT INTO board_benchmarks (board_hash, solve_time, num_moves)
        VALUES (?, ?, ?)
        ''', (board_hash, solve_time, num_moves))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Board {board_hash} already in database.")


def get_board_data():
    cur, conn = create_table()

    for _ in range(10):
        dice = tuple([random.randint(-50, 50) for _ in range(6)])
        board = rev_e.create_board(5, 0, 0, dice)
        data = benchmark_solver(board)
        insert_benchmark(cur, conn, data['board_hash'], data['solve_time'], data['num_moves'])
    
    cur.execute('SELECT * FROM board_benchmarks ORDER BY solve_time ASC')
    for row in cur.fetchall():
        print(row)
    
    conn.close()
    
    return board

if __name__ == '__main__':
    get_board_data()
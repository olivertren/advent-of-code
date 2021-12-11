import datetime
import itertools
from collections import deque

import numpy as np

from utils import get_input, print_answers


def flash(board):
    board = board + 1
    f = 0
    flashed = set()
    need_to_flash = deque()
    for i in range(10):
        for j in range(10):
            if (i, j) in flashed:
                continue
            if board[i][j] > 9:
                need_to_flash.append((i, j))
    while len(need_to_flash):
        i, j = need_to_flash.pop()
        if (i, j) in flashed:
            continue
        flashed.add((i, j))
        f += 1
        for n, m in itertools.product([-1, 0, 1], [-1, 0, 1]):
            if n == m == 0:
                continue
            if n + i < 0 or n + i >= 10:
                continue
            if m + j < 0 or m + j >= 10:
                continue
            board[i + n][j + m] += 1
            if board[i + n][j + m] > 9 and (i + n, j + m) not in flashed:
                need_to_flash.append((i + n, j + m))
    for i in range(10):
        for j in range(10):
            if board[i][j] > 9:
                board[i][j] = 0
    return f, board


def part_one(ns):
    board = [[int(n_) for n_ in n] for n in ns]
    board = np.array(board)
    total_f = 0
    for i in range(100):
        f, board = flash(board)
        total_f += f
    return total_f


def part_two(ns):
    board = [[int(n_) for n_ in n] for n in ns]
    board = np.array(board)
    f = 0
    i = 0
    while f != 100:
        i += 1
        f, board = flash(board)
    return i


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 11)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

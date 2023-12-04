import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np

from utils import get_groups, get_input, print_answers


def is_symbol(x: str):
    return (not (x.isdigit())) & (x != ".")


def is_gear(x: str):
    return x == "*"


def is_part_number(start_id, end_id, row_number, board):
    return (
        is_symbol(board[row_number][start_id])
        or is_symbol(board[row_number][end_id])
        or any(
            is_symbol(x) for x in board[max(row_number - 1, 0)][start_id : end_id + 1]
        )
        or any(
            is_symbol(x)
            for x in board[min(row_number + 1, len(board) - 1)][start_id : end_id + 1]
        )
    )


def get_gear_location(start_id, end_id, row_number, board):
    gear_idxs = [(row_number, start_id), (row_number, end_id)]
    gear_idxs.extend([(max(row_number - 1, 0), i) for i in range(start_id, end_id + 1)])
    gear_idxs.extend(
        [(min(row_number + 1, len(board) - 1), i) for i in range(start_id, end_id + 1)]
    )
    gears = []
    for i, j in gear_idxs:
        if is_gear(board[i][j]):
            gears.append((i, j))
    return gears


def part_one(ns):
    board = np.array([np.array([_n for _n in n]) for n in ns])
    total = 0
    for row_number, row in enumerate(board):
        start_id = 0
        current_number = ""
        end_id = 0
        for i, x in enumerate(row):
            end_id = i
            if x.isdigit():
                current_number += x
            else:
                if current_number:
                    number = int(current_number)
                    if is_part_number(start_id, end_id, row_number, board):
                        total += number

                current_number = ""
                start_id = i

        # if last character in row is digit
        if current_number:
            number = int(current_number)
            if is_part_number(start_id, end_id, row_number, board):
                total += number

    return total


def part_two(ns):
    board = np.array([np.array([_n for _n in n]) for n in ns])
    total = 0
    gear_number_map = defaultdict(list)
    for row_number, row in enumerate(board):
        start_id = 0
        current_number = ""
        end_id = 0
        for i, x in enumerate(row):
            end_id = i
            if x.isdigit():
                current_number += x
            else:
                if current_number:
                    number = int(current_number)
                    if is_part_number(start_id, end_id, row_number, board):
                        gears = get_gear_location(start_id, end_id, row_number, board)
                        for gear in gears:
                            gear_number_map[gear].append(number)

                current_number = ""
                start_id = i

        # if last character in row is digit
        if current_number:
            number = int(current_number)
            if is_part_number(start_id, end_id, row_number, board):
                gears = get_gear_location(start_id, end_id, row_number, board)
                for gear in gears:
                    gear_number_map[gear].append(number)

    for gear, numbers in gear_number_map.items():
        if len(numbers) == 2:
            total += numbers[0] * numbers[1]

    return total


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date.today()
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

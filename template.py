import datetime
import itertools
from collections import Counter
from functools import reduce
from operator import mul

import numpy as np

from utils import get_groups, get_input, print_answers


def part_one(i):
    pass


def part_two(i):
    pass


# def part_two(input_):
#     _initial = []
#
#     def _update_current(current, line):
#         current.append(set(line))
#
#     current = _initial
#     count = 0
#     for line in input_:
#         if len(line) == 0:
#             count += len(current)
#             current = _initial
#         else:
#             _update_current(current, line)
#     return count
#
#
# def part_one(input_):
#     _initial = []
#
#     def _update_current(current, line):
#         current.append(set(line))
#
#     current = _initial
#     count = 0
#     for line in input_:
#         if len(line) == 0:
#             count += len(current)
#             current = _initial
#         else:
#             _update_current(current, line)
#     return count


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day{datetime.date.today().day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np

from utils import get_groups, get_input, print_answers

digits_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "th3ee",
    "four": "fo4r",
    "five": "f5ve",
    "six": "s6x",
    "seven": "se7en",
    "eight": "ei8ht",
    "nine": "n9ne",
}


def get_first_digit(s: str) -> str:
    for character in s:
        if character.isdigit():
            return character
    return ""


def part_one(ns):
    total = 0
    for line in ns:
        first_digit = get_first_digit(line)
        last_digit = get_first_digit(reversed(line))
        num = int(first_digit + last_digit)
        total += num

    return total


def replace_digits(s: str) -> str:
    for dstr, rdstr in digits_map.items():
        s = s.replace(dstr, rdstr)

    return s


def part_two(ns):
    total = 0
    for line in ns:
        line_ = replace_digits(line)
        first_digit = get_first_digit(line_)
        last_digit = get_first_digit(reversed(line_))
        num = int(first_digit + last_digit)
        total += num

    return total


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date.today()
input_ = get_input(f"2023/day1test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np

from utils import get_groups, get_input, print_answers


def part_one(ns):
    total = 0
    for n in ns:
        _, cards = n.split(":")
        win, my = cards.split("|")
        win = win.strip()
        my = my.strip()
        win_set = set(int(c) for c in win.split())
        my_set = set(int(c) for c in my.split())
        num_cards = len(win_set.intersection(my_set))
        if num_cards:
            total += 2 ** (num_cards - 1)
    return total


def part_two(ns):
    card_winnings = defaultdict(int)

    for i, n in enumerate(ns):
        _, cards = n.split(":")
        win, my = cards.split("|")
        win = win.strip()
        my = my.strip()
        win_set = set(int(c) for c in win.split())
        my_set = set(int(c) for c in my.split())
        num_cards = len(win_set.intersection(my_set))

        card_winnings[i] += 1
        for j in range(i + 1, i + num_cards + 1):
            card_winnings[j] += card_winnings[i]

    return sum(card_winnings.values())


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

import datetime
from collections import Counter

import numpy as np

from utils import get_input, print_answers


def get_most_common_at_index(i, ns):
    counter = Counter(list(map(lambda x: x[i], ns)))
    return int(counter["1"] >= counter["0"])


def part_one(ns):
    counter = np.zeros(len(ns[0]))
    for i in range(len(counter)):
        counter[i] = get_most_common_at_index(i, ns)

    gamma = int("".join((counter == 1).astype(int).astype(str)), 2)
    epsilon = int("1" * len(counter), 2) ^ gamma

    return gamma * epsilon


def part_two(ns):
    o = ns
    c = ns
    i = 0
    while len(o) > 1 or len(c) > 1:
        mco = get_most_common_at_index(i, o)
        mcc = get_most_common_at_index(i, c)
        lcc = 1 ^ mcc

        o = list(filter(lambda x: str(mco) == x[i], o)) if len(o) > 1 else o
        c = list(filter(lambda x: str(lcc) == x[i], c)) if len(c) > 1 else c
        i += 1

    return int(o[0], 2) * int(c[0], 2)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 3)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

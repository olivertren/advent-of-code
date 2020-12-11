import datetime
from collections import Counter

import numpy as np

from utils import get_input, print_answers


def part_one(i):
    i = [0] + sorted(i)
    voltages = np.array(i)
    voltages_two = np.array(i.copy()[1:] + [voltages[-1] + 3])

    v = voltages_two - voltages
    c = Counter(v)
    return c.get(1) * c.get(3)


def part_two(i):
    i = sorted(i) + [max(i) + 3]

    w = {0: 1}

    for j in i:
        w[j] = w.get(j - 1, 0) + w.get(j - 2, 0) + w.get(j - 3, 0)

    return w[max(i)]


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day{datetime.date.today().day}test", int)
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__, int)
print("Actual")
print_answers_for_input(input_)

import datetime
from itertools import product

from utils import get_input, print_answers


def test(entries, v):
    for i, j in product(entries, entries):
        if i + j == v:
            return i * j


def part_one(i):
    n = 25
    preamble = i[:n]
    rest = i[n:]

    for j in rest:
        if test(preamble, j) is not None:
            preamble.pop(0)
            preamble.append(j)
        else:
            return j


def part_two(i, weakness):
    for j in range(len(i)):
        for k in range(j + 1, len(i)):
            if sum(i[j : k + 1]) == weakness:
                return max(i[j : k + 1]) + min(i[j : k + 1])


def print_answers_for_input(input_, weakness):
    p1 = part_one(input_)
    p2 = part_two(input_, weakness)

    print_answers(p1, p2)


weakness = 127
input_ = get_input(f"2020/day{datetime.date.today().day}test", int)
print("Tests")
print_answers_for_input(input_, weakness)

weakness = 21806024
input_ = get_input(__file__, int)
print("Actual")
print_answers_for_input(input_, weakness)

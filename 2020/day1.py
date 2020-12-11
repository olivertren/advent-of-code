from itertools import product

from utils import get_input, print_answers


def part_one(entries):
    for i, j in product(entries, entries):
        if i + j == 2020:
            return i * j


def part_two(entries):
    for i, j, k in product(entries, entries, entries):
        if i + j + k == 2020:
            return i * j * k


entries = get_input(__file__, int)
print_answers(part_one(entries), part_two(entries))

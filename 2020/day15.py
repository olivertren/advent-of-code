import datetime
from collections import defaultdict

from utils import get_input, print_answers


def get_n(n, i):
    num = defaultdict(list)

    init = [int(_i) for _i in i.split(",")]
    for _i, _j in enumerate(init):
        num[_j].append(_i + 1)

    _i = _i + 1

    while _i < n:
        _i = _i + 1
        seen = num[_j]

        if len(seen) == 1:
            _j = 0
        else:
            _j = seen[-1] - seen[-2]
        num[_j].append(_i)

    return _j


def part_one(i):
    return get_n(2020, i)


def part_two(i):
    return get_n(30000000, i)


def print_answers_for_input(input_):
    p1 = part_one(input_[0])
    p2 = part_two(input_[0])

    print_answers(p1, p2)


input_ = get_input(f"2020/day{datetime.date.today().day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

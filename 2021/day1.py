import datetime

from utils import get_input, print_answers


def part_one(i_, start=1):
    c = 0
    for i, j in zip(i_, i_[start:]):
        if j > i:
            c += 1
    return c


def part_two(i_):
    return part_one(i_, start=3)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 1)
input_ = get_input(f"{today.year}/day{today.day}test", int)
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__, int)
print("Actual")
print_answers_for_input(input_)

import datetime

from utils import get_input, print_answers


def part_one(ns):
    ns = [int(n) for n in ns[0].split(",")]
    return min(sum(abs(n - i) for n in ns) for i in range(min(ns), max(ns) + 1))


def part_two(ns):
    ns = [int(n) for n in ns[0].split(",")]
    return min(sum(int(abs(n * (n + 1) / 2 - i)) for n in ns) for i in range(min(ns), max(ns) + 1))


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 7)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

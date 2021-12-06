import datetime
from collections import Counter

from utils import get_input, print_answers


def part_one(ns, iterations=80):
    fish = Counter(int(n) for n in ns[0].split(","))
    for i in range(iterations):
        fish2 = Counter()
        for f, v in fish.items():
            f2 = f - 1
            if f2 == -1:
                fish2[6] += v
                fish2[8] += v
            else:
                fish2[f2] += v
        fish = fish2
    return sum(v for v in fish.values())


def part_two(ns):
    return part_one(ns, iterations=256)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 6)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

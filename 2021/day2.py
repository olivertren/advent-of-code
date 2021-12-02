import datetime

from utils import get_input, print_answers

F = "forward"
D = "down"
U = "up"


def part_one(ns):
    depth = 0
    horizontal = 0
    for n in ns:
        a, b = n.split()
        if a == F:
            horizontal += int(b)
        elif a == D:
            depth += int(b)
        else:
            depth -= int(b)
    return depth * horizontal


def part_two(ns):
    depth = 0
    horizontal = 0
    aim = 0
    for n in ns:
        a, b = n.split()
        if a == F:
            horizontal += int(b)
            depth += aim * int(b)
        elif a == D:
            aim += int(b)
        else:
            aim -= int(b)
    return depth * horizontal


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 2)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

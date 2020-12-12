import datetime

from utils import get_input, print_answers


def part_one(input_):
    location = 0 + 0j
    direction = 1 + 0j

    for dr in input_:
        d = dr[0]
        r = int(dr[1:])
        turns = r / 90

        if d == "N":
            location += r * (0 + 1j)
        elif d == "S":
            location -= r * (0 + 1j)
        elif d == "E":
            location += r
        elif d == "W":
            location -= r
        elif d == "F":
            location += r * direction
        elif d == "R":
            direction *= (0 - 1j) ** turns
        else:
            direction *= (0 + 1j) ** turns

    return abs(location.real) + abs(location.imag)


def part_two(input_):
    location = 0 + 0j
    direction = 10 + 1j

    for dr in input_:
        d = dr[0]
        r = int(dr[1:])
        turns = r / 90

        if d == "N":
            direction += r * (0 + 1j)
        elif d == "S":
            direction -= r * (0 + 1j)
        elif d == "E":
            direction += r
        elif d == "W":
            direction -= r
        elif d == "F":
            location += r * direction
        elif d == "R":
            direction *= (0 - 1j) ** turns
        else:
            direction *= (0 + 1j) ** turns

    return abs(location.real) + abs(location.imag)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day{datetime.date.today().day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

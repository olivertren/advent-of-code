import datetime

import numpy as np

from utils import get_groups, print_answers


def parse(ns):
    points, inst = ns
    points = [(int(x), int(y)) for x, y in [p.split(",") for p in points.split("\n")]]
    inst = inst.split("\n")
    return points, inst


def fold(points, inst):
    i, c = inst.split("=")
    i = i[-1]
    c = int(c)
    fold_points = []
    if i == "x":
        fold_points = [(c - abs(c - p[0]), p[1]) for p in points]
    else:
        fold_points = [(p[0], c - abs(c - p[1])) for p in points]
    return list(set(fold_points))


def part_one(ns):
    points, inst = parse(ns)
    points = fold(points, inst[0])
    return len(points)


def part_two(ns):
    points, inst = parse(ns)
    for _inst in inst:
        points = fold(points, _inst)

    rows = max(x for x, y in points) + 1
    cols = max(y for x, y in points) + 1

    pic = np.array(np.zeros((rows, cols)), dtype=str)
    for i in range(rows):
        for j in range(cols):
            if (i, j) in points:
                pic[rows - i - 1][j] = "#"
            else:
                pic[rows - i - 1][j] = "."

    return "\n" + str(pic)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 13)
input_ = get_groups(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

import datetime

from utils import get_input, print_answers


def parse(ns):
    _, xy = ns.split(": ")
    x, y = xy.split(", ")
    _, x = x.split("=")
    _, y = y.split("=")
    x = x.split("..")
    y = y.split("..")
    return [(int(x[0]), int(x[1])), (int(y[0]), int(y[1]))]


def attempt(xt, yt, x, y):
    xts, xte = xt
    yts, yte = yt
    xp = 0
    yp = 0
    max_y = 0
    hit = False
    while xp <= xte and yp >= yts:
        xp += x
        yp += y
        x -= 1 if x > 0 else x
        y -= 1
        if yp > max_y:
            max_y = yp
        if xts <= xp <= xte and yts <= yp <= yte:
            hit = True
        if x == 0 and not (xts <= xp <= xte):
            break
    return max_y if hit else None


def part_one(ns):
    xt, yt = parse(ns[0])
    max_ys = []
    for x in range(1, 172):
        for y in range(-100, 200):
            max_y = attempt(xt, yt, x, y)
            if max_y is not None:
                max_ys.append(max_y)

    return max(max_ys)


def part_two(ns):
    xt, yt = parse(ns[0])
    max_ys = []
    for x in range(1, 172):
        for y in range(-100, 200):
            max_y = attempt(xt, yt, x, y)
            if max_y is not None:
                max_ys.append(max_y)

    return len(max_ys)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 17)

input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

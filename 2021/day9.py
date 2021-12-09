import datetime

from utils import get_input, print_answers


def part_one(ns):
    a = []
    for n in ns:
        a.append([int(c) for c in n])
    c = 0
    for i, j in enumerate(a):
        for n, m in enumerate(j):
            y = True
            for s, t in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if i + s < 0:
                    continue
                if n + t < 0:
                    continue
                try:
                    if a[i + s][n + t] <= m:
                        y = False
                except Exception:
                    pass
            if y:
                c += 1 + m
    return c


def find_basin(a, i, n):
    basin = {(i, n)}
    basin2 = {"placeholder"}
    while len(basin2) != 0:
        basin2 = set()
        for i, n in basin:
            for s, t in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if i + s < 0:
                    continue
                if n + t < 0:
                    continue
                if (i + s, n + t) in basin:
                    continue
                try:
                    if a[i + s][n + t] != 9:
                        basin2.add((i + s, n + t))
                except Exception:
                    pass
        basin = basin.union(basin2)
    return len(basin)


def part_two(ns):
    a = []
    for n in ns:
        a.append([int(c) for c in n])
    basins = []
    for i, j in enumerate(a):
        for n, m in enumerate(j):
            y = True
            for s, t in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if i + s < 0:
                    continue
                if n + t < 0:
                    continue
                try:
                    if a[i + s][n + t] <= m:
                        y = False
                except Exception:
                    pass
            if y:
                basins.append(find_basin(a, i, n))
    basins = sorted(basins, reverse=True)
    return basins[0] * basins[1] * basins[2]


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 9)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

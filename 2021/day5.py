import datetime
from collections import Counter

from utils import get_input, print_answers


def parse(n):
    a, b = n.split(" -> ")
    return (int(x) for x in a.split(",")), (int(x) for x in b.split(","))


def part_one(ns):
    points = []
    for n in ns:
        start, end = parse(n)
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:
            points.extend((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        elif y1 == y2:
            points.extend((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
    point_counts = Counter(points)
    overlaps = 0
    for point, count in point_counts.items():
        if count > 1:
            overlaps += 1
    return overlaps


def part_two(ns):
    points = []
    for n in ns:
        start, end = parse(n)
        x1, y1 = start
        x2, y2 = end
        if x1 == x2:
            points.extend((x1, y) for y in range(min(y1, y2), max(y1, y2) + 1))
        elif y1 == y2:
            points.extend((x, y1) for x in range(min(x1, x2), max(x1, x2) + 1))
        elif x1 > x2:
            points.extend((x1 - i, y) for i, y in enumerate(range(y1, y2 - 1 if y2 < y1 else y2 + 1, -1 if y2 < y1 else +1)))
        else:
            points.extend((x1 + i, y) for i, y in enumerate(range(y1, y2 - 1 if y2 < y1 else y2 + 1, -1 if y2 < y1 else +1)))

    point_counts = Counter(points)
    overlaps = 0
    for point, count in point_counts.items():
        if count > 1:
            overlaps += 1
    return overlaps


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 5)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

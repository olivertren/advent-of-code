import datetime
from collections import defaultdict, deque

from utils import get_input, print_answers


def get_connections(ns):
    nodes = defaultdict(set)
    for n in ns:
        a, b = n.split("-")
        nodes[a].add(b)
        nodes[b].add(a)
    return nodes


def part_one(ns):
    nodes = get_connections(ns)

    paths = deque()
    paths.append(["start"])
    fin = 0
    while paths:
        cur = paths.pop()
        end = cur[-1]
        for neigh in nodes[end]:
            cur2 = cur[:]
            if neigh == "end":
                fin += 1
                continue
            if neigh.islower() and neigh in cur:
                continue
            cur2.append(neigh)
            paths.append(cur2)
    return fin


def part_two(ns):
    nodes = get_connections(ns)

    paths = deque()
    paths.append((["start"], False))
    fin = 0
    while paths:
        cur, small_twice = paths.pop()
        end = cur[-1]
        for neigh in nodes[end]:
            cur2 = cur[:]
            small_twice2 = small_twice
            if neigh == "start":
                continue
            if neigh == "end":
                fin += 1
                continue
            if neigh.islower() and neigh in cur2:
                if small_twice2:
                    continue
                else:
                    small_twice2 = True
            cur2.append(neigh)
            paths.append((cur2, small_twice2))
    return fin


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 12)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

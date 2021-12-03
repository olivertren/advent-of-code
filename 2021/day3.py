import datetime

import numpy as np

from utils import get_input, print_answers


def part_one(ns):
    counter = np.zeros(len(ns[0]))
    for n in ns:
        for i, b in enumerate(n):
            if b == "1":
                counter[i] += 1
            else:
                counter[i] -= 1
    gamma = ""
    epsilon = ""
    for i in counter:
        if i > 0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part_two(ns):
    i = 0
    ns2 = ns
    while len(ns) > 1:
        c = 0
        for n in ns:
            if n[i] == "1":
                c += 1
            else:
                c -= 1
        ns_ = []
        for n in ns:
            if c >= 0 and n[i] == "1":
                ns_.append(n)
            elif c < 0 and n[i] == "0":
                ns_.append(n)
        ns = ns_
        i += 1

    o = ns[0]

    ns = ns2
    i = 0
    while len(ns) > 1:
        c = 0
        for n in ns:
            if n[i] == "1":
                c += 1
            else:
                c -= 1
        ns_ = []
        for n in ns:
            if c >= 0 and n[i] == "0":
                ns_.append(n)
            elif c < 0 and n[i] == "1":
                ns_.append(n)
        ns = ns_
        i += 1

    c = ns[0]
    return int(o, 2) * int(c, 2)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 3)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

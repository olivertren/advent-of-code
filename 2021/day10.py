import datetime

import numpy as np

from utils import get_input, print_answers


def get_score(n):
    o = []
    for i in n:
        if i in {"{", "[", "(", "<"}:
            o.append(i)
            continue
        p = o.pop()
        if not p:
            return 0
        elif i == "}":
            if p != "{":
                return 1197
        elif i == "]":
            if p != "[":
                return 57
        elif i == ")":
            if p != "(":
                return 3
        elif i == ">":
            if p != "<":
                return 25137
    return 0


def part_one(ns):
    return sum(get_score(n) for n in ns)


def get_score_2(n):
    s = 0
    o = []
    for i in n:
        if i in {"{", "[", "(", "<"}:
            o.append(i)
            continue
        p = o.pop()
        if not p:
            return 0
        elif i == "}":
            if p != "{":
                return 0
        elif i == "]":
            if p != "[":
                return 0
        elif i == ")":
            if p != "(":
                return 0
        elif i == ">":
            if p != "<":
                return 0
    for i in reversed(o):
        s *= 5
        if i == "(":
            s += 1
        elif i == "[":
            s += 2
        elif i == "{":
            s += 3
        else:
            s += 4
    return s


def part_two(ns):
    return int(np.median(list(get_score_2(n) for n in ns if get_score_2(n) != 0)))


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 10)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

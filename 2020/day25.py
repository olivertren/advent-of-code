import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np
from tqdm import tqdm

from utils import get_groups, get_input, print_answers


def part_one(i_):
    cpk_ = int(i_[0])
    dpk_ = int(i_[1])

    rm = 20201227
    sn = 7

    cls = 0
    dls = 0

    cpk = 1
    while cpk != cpk_:
        cls += 1
        cpk = cpk * sn % rm

    dpk = 1

    while dpk != dpk_:
        dls += 1
        dpk = dpk * sn % rm

    dek = 1
    for i in range(dls):
        dek = dek * cpk % rm

    cek = 1
    for i in range(cls):
        cek = cek * dpk % rm

    return dek, cek, dls, cls


def part_two(i_):
    return "Click Yes"


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day25test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

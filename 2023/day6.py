import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np
from more_itertools import batched
from tqdm import tqdm

from utils import get_groups, get_input, print_answers


def part_one(ns):
    ts, ds = ns
    ts = ts.split(":")[1]
    ds = ds.split(":")[1]
    ts = map(int, ts.split())
    ds = map(int, ds.split())

    total = 1
    for t, d in zip(ts, ds):
        b = 0
        for i in range(t):
            if i * (t - i) > d:
                b += 1
        total *= b

    return total


def part_two(ns):
    ts, ds = ns
    ts = ts.split(":")[1]
    ds = ds.split(":")[1]
    t = int("".join(ts.split()))
    d = int("".join(ds.split()))

    total = 1
    b = 0
    for i in tqdm(range(t)):
        if i * (t - i) > d:
            b += 1
    total *= b

    return total


def print_answers_for_input(input_):
    p1 = part_one(input_)
    # print_answers(p1)

    p2 = part_two(input_)
    # print_answers(p2)

    print_answers(p1, p2)


input_ = get_input(f"{__file__.split('.py')[0]}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np
from more_itertools import batched
from tqdm import tqdm

from utils import get_groups, get_input, print_answers


def part_one(ns):
    pass


def part_two(ns):
    pass


def print_answers_for_input(input_):
    p1 = part_one(input_)
    print_answers(p1)

    # p2 = part_two(input_)
    # print_answers(p2)

    # print_answers(p1, p2)


input_ = get_input(f"{__file__.split('.py')[0]}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

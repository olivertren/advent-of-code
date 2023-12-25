import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np
from more_itertools import batched
from tqdm import tqdm

from utils import get_groups, get_input, print_answers


def part_one(ns):
    t = 0
    for line in ns:
        total = 0
        nums = [int(n) for n in line.split()]
        total = nums[-1]
        while nums[-1] != 0:
            nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            total += nums[-1]
        t += total

    return t


def part_two(ns):
    t = 0
    for line in ns:
        nums = [int(n) for n in line.split()]
        total = nums[0]
        coefficient = -1
        while nums[-1] != 0:
            # print(nums, coefficient, total)
            nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
            total += coefficient * nums[0]
            coefficient *= -1
        t += total
    return t


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

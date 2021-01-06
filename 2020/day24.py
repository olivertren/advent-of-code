import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np
from tqdm import tqdm

from utils import get_groups, get_input, print_answers


def part_one(i_):
    tiles = {}

    for l in i_:
        loc = (0, 0)
        idx = -1
        while idx < len(l) - 1:
            idx += 1
            current = l[idx]
            if current == "s":
                idx += 1
                current = l[idx]
                if current == "e":
                    loc = (loc[0] - 1, loc[1] + 0.5)
                else:
                    loc = (loc[0] - 1, loc[1] - 0.5)
            elif current == "n":
                idx += 1
                current = l[idx]
                if current == "e":
                    loc = (loc[0] + 1, loc[1] + 0.5)
                else:
                    loc = (loc[0] + 1, loc[1] - 0.5)
            elif current == "e":
                loc = (loc[0], loc[1] + 1)
            elif current == "w":
                loc = (loc[0], loc[1] - 1)

        if loc in tiles:
            tiles[loc] = not tiles[loc]
        else:
            tiles[loc] = True

    return sum(tiles.values())


def part_two(i_):
    tiles = {}

    for l in i_:
        loc = (0, 0)
        idx = -1
        while idx < len(l) - 1:
            idx += 1
            current = l[idx]
            if current == "s":
                idx += 1
                current = l[idx]
                if current == "e":
                    loc = (loc[0] - 1, loc[1] + 0.5)
                else:
                    loc = (loc[0] - 1, loc[1] - 0.5)
            elif current == "n":
                idx += 1
                current = l[idx]
                if current == "e":
                    loc = (loc[0] + 1, loc[1] + 0.5)
                else:
                    loc = (loc[0] + 1, loc[1] - 0.5)
            elif current == "e":
                loc = (loc[0], loc[1] + 1)
            elif current == "w":
                loc = (loc[0], loc[1] - 1)

        if loc in tiles:
            tiles[loc] = not tiles[loc]
        else:
            tiles[loc] = True

    ADJ = [(-1, -0.5), (-1, 0.5), (0, 1), (0, -1), (1, -0.5), (1, 0.5)]

    def get_adj(x, y, tiles):
        return sum([tiles.get((x + x_, y + y_), 0) for x_, y_ in ADJ])

    def get_neighbors(x, y):
        return {(x + x_, y + y_) for x_, y_ in ADJ}

    for i in tqdm(range(100)):
        new_tiles = {}
        tiles_to_check = set(tiles)
        for (x, y), value in tiles.items():
            tiles_to_check |= get_neighbors(x, y)

        for (x, y) in tiles_to_check:
            value = tiles.get((x, y), 0)
            neighbors = get_adj(x, y, tiles)
            if value:
                if neighbors == 0 or neighbors > 2:
                    new_tiles[(x, y)] = 0
                else:
                    new_tiles[(x, y)] = 1
            else:
                if neighbors == 2:
                    new_tiles[(x, y)] = 1
                else:
                    new_tiles[(x, y)] = 0
        tiles = new_tiles

    return sum(tiles.values())


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day24test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

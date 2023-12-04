import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np

from utils import get_groups, get_input, print_answers


def parse_game(game):
    _, games = game.split(":")
    cubes_list = []
    for g in games.split(";"):
        sets = g.split(",")
        game_cubes = []
        for _set in sets:
            cubes = _set.split(",")
            game_cubes.append(
                {
                    cube.strip().split(" ")[1]: int(cube.strip().split(" ")[0])
                    for cube in cubes
                }
            )
        cubes_list.append(game_cubes)
    return cubes_list


def possible_game(cubes_list):
    for game_cubes in cubes_list:
        for cubes in game_cubes:
            if cubes.get("red", 0) > 12:
                return False
            if cubes.get("green", 0) > 13:
                return False
            if cubes.get("blue", 0) > 14:
                return False
    return True


def part_one(ns):
    total = 0
    for id, game in enumerate(ns):
        parsed_game = parse_game(game)
        if possible_game(parsed_game):
            total += id + 1
    return total


def power_game(cubes_list):
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for game_cubes in cubes_list:
        for cubes in game_cubes:
            for color in min_cubes.keys():
                min_cubes[color] = max(min_cubes[color], cubes.get(color, 0))
    return min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]


def part_two(ns):
    total = 0
    for id, game in enumerate(ns):
        parsed_game = parse_game(game)
        total += power_game(parsed_game)
    return total


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date.today()
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

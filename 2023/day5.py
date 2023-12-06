import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np
import tqdm

from utils import batched, get_groups, get_input, print_answers


def generate_map(text):
    mappings = text.split("\n")[1:]
    ranges = []
    for mapping in mappings:
        dest, source, n = list(map(int, mapping.split()))
        ranges.append(
            (
                (source, source + n),
                (dest, dest + n),
                dest - source,
            )
        )
    return ranges


def part_one(ns):
    seeds = list(map(int, ns[0].split(":")[1].strip().split()))

    seed_to_soil = generate_map(ns[1])
    soil_to_fertilizer = generate_map(ns[2])
    fertilizer_to_water = generate_map(ns[3])
    water_to_light = generate_map(ns[4])
    light_to_temp = generate_map(ns[5])
    temp_to_hum = generate_map(ns[6])
    hum_to_location = generate_map(ns[7])

    def get_location(seed):
        location = seed
        for mapping in tqdm.tqdm(
            [
                seed_to_soil,
                soil_to_fertilizer,
                fertilizer_to_water,
                water_to_light,
                light_to_temp,
                temp_to_hum,
                hum_to_location,
            ]
        ):
            for source, _, diff in tqdm.tqdm(mapping):
                if source[0] <= location < source[1]:
                    location = location + diff
                    break
        return location

    return min(list(get_location(seed) for seed in seeds))


def part_two(ns):
    seeds = list(map(int, ns[0].split(":")[1].strip().split()))
    seed_ranges = list(batched(seeds, 2))

    seed_to_soil = generate_map(ns[1])
    soil_to_fertilizer = generate_map(ns[2])
    fertilizer_to_water = generate_map(ns[3])
    water_to_light = generate_map(ns[4])
    light_to_temp = generate_map(ns[5])
    temp_to_hum = generate_map(ns[6])
    hum_to_location = generate_map(ns[7])

    def get_seed(location):
        seed = location
        for mapping in reversed(
            [
                seed_to_soil,
                soil_to_fertilizer,
                fertilizer_to_water,
                water_to_light,
                light_to_temp,
                temp_to_hum,
                hum_to_location,
            ]
        ):
            for _, source, diff in mapping:
                if source[0] <= seed < source[1]:
                    seed = seed - diff
                    break
        return seed

    max_location = 0
    for _, source, _ in hum_to_location:
        if max_location < source[0]:
            max_location = source[1]

    for i in tqdm.trange(max_location):
        seed = get_seed(i)
        for _i, _j in seed_ranges:
            if _i <= seed < _i + _j:
                return i


def print_answers_for_input(input_):
    # p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p2)


today = datetime.date.today()
input_ = get_groups(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

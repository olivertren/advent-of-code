import datetime
import itertools
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce
from operator import mul
from typing import List

import numpy as np

from utils import get_groups, get_input, print_answers

LEN = 10

MONSTER = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
MONSTER = MONSTER.split("\n")[1:-1]
MONSTER_IDX = []
MONSTER_LENGTH = len(MONSTER[0])
MONSTER_HEIGHT = len(MONSTER)
MONSTER_POUNDS = 0
for i in range(MONSTER_HEIGHT):
    for j in range(MONSTER_LENGTH):
        if MONSTER[i][j] == "#":
            MONSTER_IDX.append((i, j))
            MONSTER_POUNDS += 1


def part_one(i_, num_side_tiles):
    tiles = {}
    tile_sides = {}
    flip_tile_sides = {}
    for tile in i_:
        rows = tile.split("\n")
        id = rows[0].split()[1][:-1]
        rows = rows[1:]

        tiles[id] = rows
        sides = []
        sides.append(rows[0])
        sides.append("".join([i[LEN - 1] for i in rows]))
        sides.append("".join(reversed(rows[LEN - 1])))
        sides.append("".join(reversed([i[0] for i in rows])))

        reverse_sides = []
        reverse_sides.append("".join((reversed(rows[0]))))
        reverse_sides.append("".join([i[0] for i in rows]))
        reverse_sides.append(rows[LEN - 1])
        reverse_sides.append("".join((reversed([i[LEN - 1] for i in rows]))))

        tile_sides[id] = sides
        flip_tile_sides[id] = reverse_sides

    matching_tiles = defaultdict(set)
    for i in tiles:
        for j in tiles:
            if i == j:
                continue

            for iside in tile_sides[i]:
                for jside in tile_sides[j]:
                    if iside == jside:
                        matching_tiles[i].add(j)
                        break
                for jside in flip_tile_sides[j]:
                    if iside == jside:
                        matching_tiles[i].add(f"f{j}")

    corners = []
    for id, matches in matching_tiles.items():
        if len(matches) == 2:
            corners.append(id)

    return reduce(mul, [int(i) for i in corners])


def part_two(i_, num_side_tiles):
    tiles = {}
    tile_sides = {}
    flip_tile_sides = {}

    for tile in i_:
        rows = tile.split("\n")
        id = rows[0].split()[1][:-1]
        rows = rows[1:]

        tiles[id] = rows
        sides = []
        sides.append(rows[0])
        sides.append("".join([i[LEN - 1] for i in rows]))
        sides.append("".join(reversed(rows[LEN - 1])))
        sides.append("".join(reversed([i[0] for i in rows])))

        reverse_sides = []
        reverse_sides.append("".join((reversed(rows[0]))))
        reverse_sides.append("".join([i[0] for i in rows]))
        reverse_sides.append(rows[LEN - 1])
        reverse_sides.append("".join((reversed([i[LEN - 1] for i in rows]))))

        tile_sides[id] = sides
        flip_tile_sides[id] = reverse_sides

    matching_tiles = defaultdict(set)
    for i in tiles:
        for j in tiles:
            if i == j:
                continue

            for iside in tile_sides[i]:
                for jside in tile_sides[j]:
                    if iside == jside:
                        matching_tiles[i].add(j)
                        break
                for jside in flip_tile_sides[j]:
                    if iside == jside:
                        matching_tiles[i].add(f"f{j}")

    corners = []
    for id, matches in matching_tiles.items():
        if len(matches) == 2:
            corners.append(id)

    new_map_ids = []
    seen = set()
    new_map_ids.append([corners[0]])
    current = corners[0]
    seen.add(current)

    for i in range(num_side_tiles - 1):
        possible = list(matching_tiles[current])
        for j in possible:
            if "f" not in j and j not in seen:
                if len(matching_tiles.get(j)) < 4:
                    new_map_ids[0].append(j)
                    seen.add(j)
                    current = j
                    break
            elif "f" in j and j[1:] not in seen:
                if len(matching_tiles.get(j[1:])) < 4:
                    new_map_ids[0].append(j[1:])
                    seen.add(j[1:])
                    current = j[1:]
                    break

    for i in range(num_side_tiles - 1):
        current = new_map_ids[-1][0]
        possible = list(matching_tiles[current])
        for j in possible:
            if "f" not in j and j not in seen:
                current = j
                break
            elif "f" in j and j[1:] not in seen:
                current = j[1:]
                break

        new_map_ids.append([current])
        seen.add(current)
        for __ in range(num_side_tiles - 1):
            possible = list(matching_tiles[current])
            for j in possible:
                if "f" not in j and j not in seen:
                    ms = matching_tiles.get(j)
                    ms_neighbors = set()
                    for n in ms:
                        if "f" in n:
                            ms_neighbors.add(n[1:])
                        else:
                            ms_neighbors.add(n)

                    if len(ms_neighbors.intersection(seen)) == 2:
                        new_map_ids[i + 1].append(j)
                        seen.add(j)
                        current = j
                        break

                elif "f" in j and j[1:] not in seen:
                    ms = matching_tiles.get(j[1:])

                    ms_neighbors = set()
                    for n in ms:
                        if "f" in n:
                            ms_neighbors.add(n[1:])
                        else:
                            ms_neighbors.add(n)

                    if len(ms_neighbors.intersection(seen)) == 2:
                        new_map_ids[i + 1].append(j[1:])
                        seen.add(j[1:])
                        current = j[1:]
                        break

    def flip_tile(tile):
        return ["".join(reversed(i)) for i in tile]

    def rotate_cw(tile):
        return ["".join([tile[i][j] for i in range(len(tile) - 1, -1, -1)]) for j in range(0, len(tile))]

    def compare_tiles(left, right):
        left_right_edge = [i[-1] for i in left]
        right_left_edge = [i[0] for i in right]

        # print("\n")
        # print(left, right)
        # print(left_right_edge)
        # print(right_left_edge)
        # print("".join(left_right_edge) == ("".join(right_left_edge)))

        return ("".join(left_right_edge)) == ("".join(right_left_edge))

    def add_tile(left, right):
        return ["".join([left[i], right[i]]) for i in range(LEN)]

    first_tile = tiles[corners[0]]

    zero_row = new_map_ids[0]
    second_tile = tiles[zero_row[1]]

    def match_two_tiles(first_tile, second_tile):
        for _ in range(2):
            for __ in range(4):
                for ___ in range(2):
                    for ____ in range(4):
                        if compare_tiles(first_tile, second_tile):
                            return first_tile
                        second_tile = rotate_cw(second_tile)
                    second_tile = flip_tile(second_tile)
                first_tile = rotate_cw(first_tile)
            first_tile = flip_tile(first_tile)

    new_map = match_two_tiles(first_tile, second_tile)
    if zero_row[1] == "2311" or zero_row[1] == "3677":
        new_map = flip_tile((rotate_cw(rotate_cw(new_map))))

    print(corners[0])
    print(zero_row[1])

    def find_match(row_map, tile):
        for _ in range(2):
            for __ in range(4):
                if compare_tiles(row_map, tile):
                    return tile
                tile = rotate_cw(tile)
            tile = flip_tile(tile)

    def build_row(row_ids, row_map):
        for id_ in row_ids[1:]:
            tile = tiles[id_]
            row_map = add_tile(row_map, find_match(row_map, tile))
            # print(row_map)

        return row_map

    _new_map = deepcopy(new_map)
    new_map = build_row(zero_row, new_map)

    # print(new_map)

    for i in range(1, num_side_tiles):
        row_ids = new_map_ids[i]
        previous_bottom_first_tile = new_map[-1][:LEN]

        first_tile = tiles[row_ids[0]]
        for _ in range(2):
            for __ in range(4):
                if first_tile[0] == previous_bottom_first_tile:
                    row_tiles = deepcopy(first_tile)
                first_tile = rotate_cw(first_tile)
            first_tile = flip_tile(first_tile)

        row_tiles = build_row(row_ids, row_tiles)

        new_map.extend(row_tiles)

    def prune_map(new_map):
        pruned_map = []
        for i in range(LEN * num_side_tiles):
            if (i % LEN == 0) or ((i % LEN) == (LEN - 1)):
                continue

            row = new_map[i]
            pruned_map.append("")
            for j in range(LEN * num_side_tiles):
                if (j % LEN == 0) or ((j % LEN) == (LEN - 1)):
                    continue

                pruned_map[-1] += row[j]

        return pruned_map

    pruned_map = prune_map(new_map)
    number_of_pounds = sum([i.count("#") for i in pruned_map])

    def check_monster(x, y):
        for i, j in MONSTER_IDX:
            try:
                if pruned_map[x + i][y + j] != "#":
                    return False
            except IndexError:
                return False
        return True

    pruned_map_side_length = len(pruned_map)

    for _ in range(2):
        for __ in range(4):
            num_monster = 0
            for x in range(pruned_map_side_length):
                for y in range(pruned_map_side_length):
                    num_monster += check_monster(x, y)

            print(number_of_pounds)
            print(num_monster)
            if num_monster != 0:
                return number_of_pounds - MONSTER_POUNDS * num_monster
            else:
                pruned_map = rotate_cw(pruned_map)

        pruned_map = flip_tile(pruned_map)


def print_answers_for_input(input_, n):
    p1 = part_one(input_, n)
    p2 = part_two(input_, n)

    print_answers(p1, p2)


input_ = get_groups(f"2020/day20test")
print("Tests")
print_answers_for_input(input_, 3)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_, 12)

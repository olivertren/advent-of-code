import datetime
import itertools
import json
import math

from utils import get_input, print_answers


class Snailfish:
    def __init__(self, linked_list):
        self.linked_list = linked_list

    def __repr__(self):
        return str(self.linked_list)


class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    @property
    def prefix(self):
        return self.index[:-1]

    @property
    def depth(self):
        return len(self.prefix)

    def __repr__(self):
        return f"({self.index}, {self.value})"


def get_snailfishes(ns):
    snailfishes = [json.loads(n) for n in ns]
    snailfishes = [Snailfish(generate_linked_list(sf)) for sf in snailfishes]
    return snailfishes


def generate_linked_list(sf, prefix=[]):
    nsf = []
    for i, val in enumerate(sf):
        if isinstance(val, int):
            nsf.append(Node(prefix + [i], val))
        else:
            nsf.extend(generate_linked_list(val, prefix + [i]))
    return nsf


def add(sf1, sf2):
    left = [Node([0] + n.index, n.value) for n in sf1.linked_list]
    right = [Node([1] + n.index, n.value) for n in sf2.linked_list]
    sf3 = Snailfish(left + right)
    expand = True
    while expand:
        has_explode, has_split = False, False
        sf3, has_explode = explode(sf3)
        if has_explode:
            continue
        sf3, has_split = split(sf3)
        if has_split:
            continue
        expand = False

    return sf3


def explode(sf):
    has_explode = False
    for i, node1 in enumerate(sf.linked_list[:-1]):
        if node1.depth >= 4:
            node2 = sf.linked_list[i + 1]
            if is_pair(node1, node2):
                if i == 0:
                    left = []
                else:
                    left_neighbor = sf.linked_list[i - 1]
                    left = sf.linked_list[: i - 1] + [Node(left_neighbor.index, left_neighbor.value + node1.value)]

                if i + 1 == len(sf.linked_list) - 1:
                    right = []
                else:
                    right_neighbor = sf.linked_list[i + 2]
                    right = [Node(right_neighbor.index, right_neighbor.value + node2.value)] + sf.linked_list[i + 3 :]

                sf.linked_list = left + [Node(node1.prefix, 0)] + right
                has_explode = True
                break

    return sf, has_explode


def is_pair(node1, node2):
    return node1.prefix == node2.prefix


def split(sf):
    has_split = False
    for i, node in enumerate(sf.linked_list):
        if node.value >= 10:
            x, y = math.floor(node.value / 2), math.ceil(node.value / 2)
            sf.linked_list = sf.linked_list[:i] + [Node(node.index + [0], x), Node(node.index + [1], y)] + sf.linked_list[i + 1 :]
            has_split = True
            break

    return sf, has_split


def magnitude(sf):
    linked_list = sf.linked_list
    while len(linked_list) > 1:
        for i in range(len(linked_list) - 1):
            node1 = linked_list[i]
            node2 = linked_list[i + 1]
            if node1.prefix == node2.prefix:
                linked_list = linked_list[:i] + [Node(node1.prefix, 3 * node1.value + 2 * node2.value)] + linked_list[i + 2 :]
                break

    return linked_list[0].value


def part_one(ns):
    snailfishes = get_snailfishes(ns)
    snailfish = snailfishes[0]
    for sf in snailfishes[1:]:
        snailfish = add(snailfish, sf)

    return magnitude(snailfish)


def part_two(ns):
    snailfishes = get_snailfishes(ns)
    max_magnitude = 0
    for sf1, sf2 in itertools.combinations(snailfishes, 2):
        if (m := magnitude(add(sf1, sf2))) > max_magnitude:
            max_magnitude = m
        if (m := magnitude(add(sf2, sf1))) > max_magnitude:
            max_magnitude = m

    return max_magnitude


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 18)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

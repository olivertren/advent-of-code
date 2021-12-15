import datetime

import networkx as nx

from utils import get_input, print_answers

ADJ = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_weight(ns, node):
    i, j = node
    r = len(ns[0])
    c = len(ns)
    original_i, original_j = (i % r, j % c)
    weight = (int(ns[original_i][original_j]) + (i // r) + (j // c)) % 9
    weight = weight if weight else 9
    return weight


def create_graph(ns, repeats=1):
    G = nx.DiGraph()
    cols = repeats * len(ns)
    rows = repeats * len(ns[0])

    for i in range(rows):
        for j in range(cols):
            current = (i, j)
            c_weight = get_weight(ns, current)
            for n, m in ADJ:
                if not (0 <= i + n < rows):
                    continue
                if not (0 <= j + m < cols):
                    continue
                neighbor = (i + n, j + m)
                n_weight = get_weight(ns, neighbor)
                G.add_edge(current, neighbor, weight=int(n_weight))
                G.add_edge(neighbor, current, weight=int(c_weight))

    return G


def part_one(ns, repeats=1):
    rows = repeats * len(ns[0])
    cols = repeats * len(ns)
    G = create_graph(ns, repeats=repeats)
    return nx.shortest_path_length(G, source=(0, 0), target=(rows - 1, cols - 1), weight="weight")


def part_two(ns):
    return part_one(ns, repeats=5)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 15)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

import datetime
import itertools
from collections import Counter, defaultdict, deque
from functools import reduce
from operator import mul

import numpy as np

from utils import get_groups, get_input, print_answers


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A recursive function used by topologicalSort

    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Push current vertex to stack which stores result
        stack.insert(0, v)

        # The function to do Topological Sort. It uses recursive

    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Print contents of stack
        return stack


def part_one(i_):
    rules = i_[0].split("\n")

    rule_dict = {}
    rule_ns = set()
    seen_ns = set()

    rule_map = {}

    for r in rules:
        n, l = r.split(": ")
        rule_map[n] = l

        if '"' in r:
            n, l = r.split(': "')
            rule_dict[n] = {l[:-1]}
            seen_ns.add(n)
        else:
            n, l = r.split(": ")
        rule_ns.add(n)

    graph = Graph(len(rule_ns))
    for r, l in rule_map.items():
        # print(r, l)
        if '"' in l:
            continue
        else:
            letters = set()
            # print(l)
            for _r in l.lstrip().rstrip().split(" | "):
                # print(_r)
                for _l in _r.split(" "):
                    if len(_l) > 0:
                        letters.add(_l)
            for letter in letters:
                graph.addEdge(int(letter), int(r))

    # print(graph.graph[0])
    order = graph.topologicalSort()

    def get_rule(l):
        rules = l.split(" | ")
        possibles = set()

        # print(l)
        for r in rules:
            # print(r)
            r_possibles = {""}
            ls = r.split(" ")
            # print(ls)
            for l in ls:
                ls_possible = rule_dict[l]
                # print(ls_possible)
                _r_possible = set()
                for i in ls_possible:
                    for j in r_possibles:
                        _r_possible.add(j + i)
                r_possibles = _r_possible
                # print(r_possibles)
            possibles.update(r_possibles)
        return possibles

    # print(rule_map.keys())
    # print(order)
    for letter in order:
        l = rule_map[str(letter)]
        if '"' in l:
            continue
        else:
            rule_dict[str(letter)] = get_rule(l)
            # print(str(letter), rule_dict[str(letter)])

    # print(rule_dict)

    possible = rule_dict["0"]
    messages = i_[1].split("\n")

    # print(possible)

    return len(list(filter(lambda m: m in possible, messages)))


def part_two(i_):
    rules = i_[0].split("\n")

    rule_dict = {}
    rule_ns = set()
    seen_ns = set()

    rule_map = {}

    for _i, r in enumerate(rules):
        n, l = r.split(": ")
        if n == "8":
            l = "42 | 42 8"
            rules[_i] = "8: 42 | 42 8"
        elif n == "11":
            l = "42 31 | 42 11 31"
            rules[_i] = "11: 42 31 | 42 11 31"
        rule_map[n] = l

        if '"' in r:
            n, l = r.split(': "')
            rule_dict[n] = {l[:-1]}
            seen_ns.add(n)
        else:
            n, l = r.split(": ")
        rule_ns.add(n)

    graph = Graph(len(rule_ns))
    for r, l in rule_map.items():
        # print(r, l)
        if '"' in l:
            continue
        else:
            letters = set()
            # print(l)
            for _r in l.lstrip().rstrip().split(" | "):
                # print(_r)
                for _l in _r.split(" "):
                    if len(_l) > 0:
                        letters.add(_l)
            for letter in letters:
                graph.addEdge(int(letter), int(r))

    # print(graph.graph[0])
    order = graph.topologicalSort()

    def get_rule(l):
        rules = l.split(" | ")
        possibles = set()

        # print(l)
        for r in rules:
            # print(r)
            r_possibles = {""}
            ls = r.split(" ")
            # print(ls)
            for l in ls:
                ls_possible = rule_dict[l]
                # print(ls_possible)
                _r_possible = set()
                for i in ls_possible:
                    for j in r_possibles:
                        _r_possible.add(j + i)
                r_possibles = _r_possible
                # print(r_possibles)
            possibles.update(r_possibles)
        return possibles

    # print(rule_map.keys())
    # print(order)
    for letter in order[:-3]:
        l = rule_map[str(letter)]
        if '"' in l:
            continue
        else:
            rule_dict[str(letter)] = get_rule(l)
            # print(str(letter), rule_dict[str(letter)])

    forty_two = rule_dict["42"]

    thirty_one = rule_dict["31"]

    # print(rule_dict)

    # possible = rule_dict["0"]
    messages = i_[1].split("\n")

    def is_possible(m):
        if len(m) % 8 != 0:
            return False

        chunks, chunk_size = len(m), 8
        chunks = [m[i : i + chunk_size] for i in range(0, chunks, chunk_size)]
        # print(chunks)
        chunks.reverse()

        for i in range(1, len(m) // 16 + 1):
            thirty_ones = chunks[:i]
            forty_twos = chunks[i:]

            if len(forty_twos) <= len(thirty_ones):
                return False

            # if len(m) == 32:
            #     print(f"31 {thirty_ones}")
            #     print(f"42 {forty_twos}")

            if all([to in thirty_one for to in thirty_ones]) and all([ft in forty_two for ft in forty_twos]):
                return True

        return False

    # print(possible)

    return len(list(filter(lambda m: is_possible(m), messages)))


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_groups(f"2020/day19test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

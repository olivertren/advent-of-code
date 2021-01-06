import datetime
import itertools
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import reduce
from operator import mul

import numpy as np

from utils import get_groups, get_input, print_answers


def part_one(i_):
    p1 = deque([int(_) for _ in i_[0].split("\n")[1:]])
    p2 = deque([int(_) for _ in i_[1].split("\n")[1:]])

    while len(p1) > 0 and len(p2) > 0:
        p1_card = p1.popleft()
        p2_card = p2.popleft()

        if p1_card > p2_card:
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            p2.append(p2_card)
            p2.append(p1_card)

    def get_score(p):
        score = 0
        for i, j in enumerate(reversed(p)):
            score += (i + 1) * j
        return score

    return get_score(p1) or get_score(p2)


def part_two(i_):
    p1 = deque([int(_) for _ in i_[0].split("\n")[1:]])
    p2 = deque([int(_) for _ in i_[1].split("\n")[1:]])

    def play_game(round, p1, p2):
        seen_decks = set()
        p1 = deepcopy(p1)
        p2 = deepcopy(p2)

        while len(p1) > 0 and len(p2) > 0:
            p1_deck = ",".join([str(i) for i in p1])
            p2_deck = ",".join([str(i) for i in p2])

            if (p1_deck, p2_deck) in seen_decks:
                return True, p1, p2
            seen_decks.add((p1_deck, p2_deck))

            p1_card = p1.popleft()
            p2_card = p2.popleft()

            if p1_card <= len(p1) and p2_card <= len(p2):
                if play_game(round + 1, deque(list(p1)[:p1_card]), deque(list(p2)[:p2_card]))[0]:
                    p1.append(p1_card)
                    p1.append(p2_card)
                    continue
                else:
                    p2.append(p2_card)
                    p2.append(p1_card)
                    continue
            else:
                if p1_card > p2_card:
                    p1.append(p1_card)
                    p1.append(p2_card)
                else:
                    p2.append(p2_card)
                    p2.append(p1_card)

        if len(p1) > len(p2):
            return True, p1, p2
        else:
            return False, p1, p2

    winner, p1, p2 = play_game(0, p1, p2)

    def get_score(p):
        score = 0
        for i, j in enumerate(reversed(p)):
            score += (i + 1) * j
        return score

    print(winner, p1, p2)
    return get_score(p1), get_score(p2)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_groups(f"2020/day22test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

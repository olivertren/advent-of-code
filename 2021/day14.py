import datetime
from collections import Counter

from utils import get_groups, print_answers


def parse(ns):
    template, rules = ns
    rules = [r.split(" -> ") for r in rules.split("\n")]
    rules = {r[0]: r[1] for r in rules}

    return template, rules


def iterate(template, rules):
    output = ""
    for i, j in zip(template, template[1:]):
        output += i
        if i + j in rules:
            output += rules[i + j]
    output += template[-1]
    return output


def part_one(ns):
    template, rules = parse(ns)
    for i in range(10):
        template = iterate(template, rules)

    c = Counter(template)
    mc = c.most_common()
    return mc[0][1] - mc[-1][1]


def template_to_pairs(template):
    pairs = Counter()
    for i, j in zip(template, template[1:]):
        pairs[i + j] += 1
    return pairs


def iterate2(pairs, rules):
    new_pairs = Counter()
    for pair, num in pairs.items():
        if pair not in rules:
            new_pairs[pair] += num
        a, c = pair
        b = rules[pair]
        new_pairs[a + b] += num
        new_pairs[b + c] += num
    return new_pairs


def part_two(ns):
    template, rules = parse(ns)
    pairs = template_to_pairs(template)

    for i in range(40):
        pairs = iterate2(pairs, rules)

    # every letter is double counted except for first and last
    c = Counter()
    for pair, num in pairs.items():
        c[pair[0]] += num
        c[pair[1]] += num
    c[template[0]] += 1
    c[template[-1]] += 1
    mc = c.most_common()
    return int((mc[0][1] - mc[-1][1]) / 2)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 14)
input_ = get_groups(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

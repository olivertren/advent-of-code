from collections import Counter, defaultdict

from utils import get_groups, print_answers


def name_and_bounds_for_rule(rule):
    name, b = rule.split(": ")
    a, b = b.split(" or ")
    _l0, _h0 = a.split("-")
    _l1, _h1 = b.split("-")

    _l0 = int(_l0)
    _h0 = int(_h0)
    _l1 = int(_l1)
    _h1 = int(_h1)

    return name, _l0, _h0, _l1, _h1


def part_one(i):
    rules = i[0]
    near = i[2]

    valids = set()

    for rule in rules.split("\n"):
        _, _l0, _h0, _l1, _h1 = name_and_bounds_for_rule(rule)

        for v in range(_l0, _h0 + 1):
            valids.add(v)
        for v in range(_l1, _h1 + 1):
            valids.add(v)

    invalids = Counter()
    for ticket in near.split("\n")[1:]:
        ticket_nums = [int(_n) for _n in ticket.split(",")]
        for n in ticket_nums:
            if n not in valids:
                invalids[n] += 1

    return sum([k * v for k, v in invalids.items()])


def part_two(i):
    rules = i[0].split("\n")
    you = i[1]
    near = i[2]

    valids = set()
    valids_by_rule = defaultdict(set)

    for rule in rules:
        name, _l0, _h0, _l1, _h1 = name_and_bounds_for_rule(rule)

        for v in range(_l0, _h0 + 1):
            valids_by_rule[name].add(v)
            valids.add(v)
        for v in range(_l1, _h1 + 1):
            valids_by_rule[name].add(v)
            valids.add(v)

    column_ticket_numbers = defaultdict(set)
    for ticket in near.split("\n")[1:]:
        ticket_numbers = [int(n) for n in ticket.split(",")]
        for n in ticket_numbers:
            if n not in valids:
                break
        else:
            for _i, _j in enumerate(ticket_numbers):
                column_ticket_numbers[_i].add(_j)

    possible_rules = defaultdict(set)
    for col, nums in column_ticket_numbers.items():
        for rule, valid_nums in valids_by_rule.items():
            if nums.issubset(valid_nums):
                possible_rules[col].add(rule)

    departure_columns = set()
    used_rules = set()
    num_rules = len(rules)

    while len(used_rules) < num_rules:
        for col, rules in possible_rules.items():
            if len(rules) > 1:
                continue

            rules = rules - used_rules
            rule = rules.pop()
            used_rules.add(rule)

            if "departure" in rule:
                departure_columns.add(col)

            del possible_rules[col]

            break

        for col in possible_rules:
            possible_rules[col].difference_update({rule})

    prod = 1

    your_ticket_numbers = [int(_i) for _i in you.split("\n")[1].split(",")]

    for col in departure_columns:
        prod *= your_ticket_numbers[col]

    return prod


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_groups(f"2020/day16test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

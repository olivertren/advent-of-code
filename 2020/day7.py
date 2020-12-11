from utils import get_input, print_answers

GOLD = "shiny gold"


def part_one(bags):
    contains_shiny_gold = {}

    def _has_gold(color):
        if color in contains_shiny_gold:
            return True
        else:
            for (number, child_color) in bags[color]:
                if child_color == GOLD:
                    contains_shiny_gold[color] = number
                    return True
                elif _has_gold(child_color):
                    contains_shiny_gold[color] = 1
                    return True
        return False

    return sum([_has_gold(color) for color in bags])


def part_two(bags):
    sub_bags = {}
    for color in bags:
        if len(bags.get(color)) == 0:
            sub_bags[color] = 1

    print(sub_bags)

    def _get_sub_bags(color):
        if color in sub_bags:
            return sub_bags[color]
        else:
            num_sub_bags = sum([number * _get_sub_bags(color) for number, color in bags.get(color)]) + 1
            sub_bags[color] = num_sub_bags
            return num_sub_bags

    count = _get_sub_bags(GOLD)
    return count - 1


input_ = get_input(__file__)
# input_ = get_input(f"2020/day{datetime.date.today().day}test2")

bags = {}


def _parse_rule(rule):
    color, children = rule.split("contain")
    color = color.split("bags")[0].strip()

    children = children.split(", ")

    def _parse_child(child):
        child = child.split("bag")[0]
        child = child.lstrip()
        number, _, color = child.partition(" ")
        color = color.strip()
        number = int(number) if number != "no" else 0
        return number, color

    children = [_parse_child(child) for child in children if _parse_child(child)[0]]

    bags[color] = children


for rule in input_:
    _parse_rule(rule)

p1 = part_one(bags)
p2 = part_two(bags)

print_answers(p1, p2)

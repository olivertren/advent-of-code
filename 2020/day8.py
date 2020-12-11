import datetime

from utils import get_input, print_answers


def part_one(input_):
    current = 0
    seen = set()
    index = 0

    def run_inst(index, current):
        inst, value = input_[index].split()
        value = int(value[1:]) if value[0] == "+" else -1 * int(value[1:])
        seen.add(index)
        if inst == "nop":
            return index + 1, current
        if inst == "acc":
            current += value
            return index + 1, current
        if inst == "jmp":
            return index + value, current

    num_inst = len(input_)
    while index not in seen:
        index, current = run_inst(index, current)
        if index >= num_inst:
            return True, current

    return False, current


def part_two(input_):
    for i, rule in enumerate(input_):
        rules = input_.copy()
        inst, value = rules[i].split()
        if value == "+0" or value == "-0":
            continue
        else:
            if inst == "jmp":
                rules[i] = "nop " + value
            elif inst == "nop":
                rules[i] = "jmp " + value
            else:
                continue

        if (value := part_one(rules))[0] is not False:
            return value[1]


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1[1], p2)


input_ = get_input(f"2020/day{datetime.date.today().day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

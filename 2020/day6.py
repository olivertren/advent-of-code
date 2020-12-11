import string

from utils import get_input, print_answers


def part_one(input_):
    answer_set = set()
    count = 0
    for line in input_:
        if len(line) == 0:
            count += len(answer_set)
            answer_set = set()
        else:
            answer_set = answer_set.union(set(line))
    return count


def part_two(input_):
    answer_set = set(string.ascii_lowercase)
    count = 0
    for line in input_:
        if len(line) == 0:
            count += len(answer_set)
            answer_set = set(string.ascii_lowercase)
        else:
            answer_set = answer_set.intersection(set(line))
    return count


input_ = get_input(__file__)
input_.append("")

p1 = part_one(input_)
p2 = part_two(input_)
print_answers(p1, p2)

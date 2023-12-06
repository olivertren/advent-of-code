import itertools
import os


def get_input(filename, parse_func=lambda x: x):
    lines = []
    directory = os.path.dirname(filename)
    filename = os.path.splitext(os.path.basename(filename))[0]
    with open(f"{directory}/inputs/{filename}.txt") as f:
        for line in f:
            lines.append(parse_func(line.strip()))
    return lines


def get_groups(filename):
    directory = os.path.dirname(filename)
    filename = os.path.splitext(os.path.basename(filename))[0]
    input_ = ""
    with open(f"{directory}/inputs/{filename}.txt") as f:
        for line in f:
            input_ += line
    groups = input_.split("\n\n")
    groups = [g.strip() for g in groups]
    return groups


def print_answers(part_one=None, part_two=None):
    print(f"Part One: {part_one}")
    print(f"Part Two: {part_two}")


def batched(iterable, n):
    iterator = iter(iterable)
    while True:
        chunk = list(itertools.islice(iterator, n))
        if not chunk:
            return
        yield chunk

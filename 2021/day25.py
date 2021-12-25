import datetime

from utils import get_input, print_answers


def parse(ns):
    rows = len(ns)
    cols = len(ns[0])
    east = set()
    south = set()

    for x, row in enumerate(ns):
        for y, cell in enumerate(row):
            if cell == ">":
                east.add((x, y))
            if cell == "v":
                south.add((x, y))

    occupied = east | south
    return rows, cols, east, south, occupied


def part_one(ns):
    rows, cols, east, south, occupied = parse(ns)
    no_move = False
    i = 0
    while not no_move:
        i += 1
        east_movers = set()
        new_east_positions = set()
        for x, y in east:
            y2 = (y + 1) % cols
            if (x, y2) in occupied:
                continue
            else:
                east_movers.add((x, y))
                new_east_positions.add((x, y2))
        east = (east - east_movers) | new_east_positions
        occupied = (occupied - east_movers) | new_east_positions

        south_movers = set()
        new_south_positions = set()
        for x, y in south:
            x2 = (x + 1) % rows
            if (x2, y) in occupied:
                continue
            else:
                south_movers.add((x, y))
                new_south_positions.add((x2, y))
        south = (south - south_movers) | new_south_positions
        occupied = (occupied - south_movers) | new_south_positions
        if len(south_movers | east_movers) == 0:
            no_move = True

    return i


def part_two(ns):
    pass


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 25)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

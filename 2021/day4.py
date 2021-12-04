import datetime

from utils import get_groups, print_answers


def has_bingo(matched):
    for i in range(0, 5):
        if set(range(i * 5, i * 5 + 5)).issubset(matched):
            return True
        if set([i, 5 + i, 10 + i, 15 + i, 20 + i]).issubset(matched):
            return True


def part_one(ns):
    bingo = ns[0].split(",")
    boards = ns[1:]
    numbers = []
    matched = [set() for i in range(len(boards))]
    for board in boards:
        b = []
        rows = board.split("\n")
        for r in rows:
            b.extend(r.split())
        numbers.append(b)

    for b in bingo:
        for i, n in enumerate(numbers):
            try:
                matched[i].add(n.index(b))
            except Exception:
                pass
            if has_bingo(matched[i]):
                total = sum(map(lambda x: int(x), n))
                marked = sum(int(n[j]) for j in matched[i])

                return int(b) * (total - marked)


def part_two(ns):
    bingo = ns[0].split(",")
    boards = ns[1:]
    numbers = []
    matched = [set() for i in range(len(boards))]
    for board in boards:
        b = []
        rows = board.split("\n")
        for r in rows:
            b.extend(r.split())
        numbers.append(b)

    for b in bingo:
        for i, n in enumerate(numbers):
            try:
                matched[i].add(n.index(b))
            except Exception:
                pass
            if all(has_bingo(m) for m in matched):
                total = sum(map(lambda x: int(x), n))
                marked = sum(int(n[j]) for j in matched[i])

                return int(b) * (total - marked)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 4)
input_ = get_groups(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

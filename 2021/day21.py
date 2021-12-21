import datetime

from utils import get_input, print_answers


def parse(ns):
    p1 = ns[0].split(": ")[1]
    p2 = ns[1].split(": ")[1]
    return int(p1), int(p2)


def part_one(ns):
    p1, p2 = parse(ns)
    s1, s2 = 0, 0
    i = 0
    while s1 < 1000 and s2 < 1000:
        d1 = i % 100 + 1
        i += 1
        d2 = i % 100 + 1
        i += 1
        d3 = i % 100 + 1
        i += 1
        if (i / 3) % 2 == 1:
            p1 = (p1 + d1 + d2 + d3 - 1) % 10 + 1
            s1 += p1
        else:
            p2 = (p2 + d1 + d2 + d3 - 1) % 10 + 1
            s2 += p2
    return i * min(s1, s2)


outcomes = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}


def part_two(ns):
    p1, p2 = parse(ns)
    s1, s2 = 0, 0
    i = 0

    f1 = 0
    f2 = 0
    games = [(p1, s1, p2, s2, 1)]
    i = 0
    while games:
        i += 1
        new_games = []
        if i % 2 == 1:
            for p1, s1, p2, s2, n in games:
                for r, nr in outcomes.items():
                    np1 = (p1 + r - 1) % 10 + 1
                    ns1 = s1 + np1
                    if ns1 >= 21:
                        f1 += n * nr
                    else:
                        new_games.append((np1, ns1, p2, s2, n * nr))
        else:
            for p1, s1, p2, s2, n in games:
                for r, nr in outcomes.items():
                    np2 = (p2 + r - 1) % 10 + 1
                    ns2 = s2 + np2
                    if ns2 >= 21:
                        f2 += n * nr
                    else:
                        new_games.append((p1, s1, np2, ns2, n * nr))
        games = new_games

    return max(f1, f2)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 21)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

import datetime

from utils import get_input, print_answers


def part_one(i):
    b = {}
    for line in i:
        start = 36 * ["0"]
        if "mask" in line:
            _, m = line.split("=")
            m = m.strip().lstrip()
        else:
            mem, num = line.split("=")
            num = bin(int(num.strip().lstrip()))[2:]
            loc = int(mem.strip()[4:-1])

            for n, j in enumerate(num[::-1]):
                start[n] = j
            for n, j in enumerate(m[::-1]):
                if j != "X":
                    start[n] = j

            b_ = int("".join(start[::-1]), 2)
            b[loc] = b_

    return sum(b.values())


def part_two(i):
    b = {}
    for line in i:
        start = 36 * ["0"]
        if "mask" in line:
            _, m = line.split("=")
            m = m.strip().lstrip()
        else:
            mem, num = line.split("=")
            num = int(num.strip().lstrip())
            loc = bin(int(mem.strip()[4:-1]))[2:]

            s = start.copy()
            for n, j in enumerate(loc[::-1]):
                s[n] = j
            v = [s]

            for n, j in enumerate(m[::-1]):
                if j == "1":
                    for _i, s in enumerate(v):
                        s[n] = j
                        v[_i] = s
                elif j == "X":
                    v_ = []
                    for _i, s in enumerate(v):
                        s0 = s.copy()
                        s0[n] = "0"
                        s1 = s.copy()
                        s1[n] = "1"
                        v_.append(s0)
                        v_.append(s1)
                    v = v_
            for s in v:
                b_ = int("".join(s[::-1]), 2)
                b[b_] = num

    return sum(b.values())


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day{datetime.date.today().day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

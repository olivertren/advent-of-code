import datetime

from utils import get_input, print_answers


def part_one(ns):
    c = {1: 2, 4: 4, 7: 3, 8: 7}
    lens = c.values()
    co = 0
    for n in ns:
        n = n.split(" | ")[1]
        n = n.split()
        for m in n:
            if len(m) in lens:
                co += 1
    return co


def map_line(n):
    mapping = {}

    n, m = n.split(" | ")
    n = n.split()
    m = m.split()
    n = sorted(n, key=lambda x: len(x))

    # number - number of letters
    # 1 - 2
    one = n[0]
    # 7 - 3
    seven = n[1]
    # 4 - 4
    four = n[2]
    # 2 - 5
    two = n[3]
    # 3 - 5
    three = n[4]
    # 5 - 5
    five = n[5]
    # 0 - 6
    zero = n[6]
    # 6 - 6
    six = n[7]
    # 9 - 6
    nine = n[8]
    # 8 - 7
    eight = n[9]

    # know 1, 4, 7, 8
    # find six
    if len(set(one) - set(six)) == 1:
        pass
    elif len(set(one) - set(zero)) == 1:
        zero, six = six, zero
    else:
        nine, six = six, nine

    # know 1, 4, 6, 7, 8
    # find three
    if (set(one) - set(three)) == set():
        pass
    elif (set(one) - set(two)) == set():
        two, three = three, two
    else:
        three, five = five, three

    # know 1, 3, 4, 6, 7, 8
    # find zero and nine
    if (set(four) - set(nine)) == set():
        pass
    else:
        zero, nine = nine, zero

    # know 0, 1, 3, 4, 6, 7, 8, 9
    # find two and five
    if (set(five) - set(six)) == set():
        pass
    else:
        two, five = five, two

    # know 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    mapping = {zero: "0", one: "1", two: "2", three: "3", four: "4", five: "5", six: "6", seven: "7", eight: "8", nine: "9"}

    sorted_mapping = {"".join(sorted(k)): v for k, v in mapping.items()}
    return int("".join(sorted_mapping["".join(sorted(i))] for i in m))


def part_two(ns, p):
    if p:
        print(list(map_line(n) for n in ns))
    return sum(map_line(n) for n in ns)


def print_answers_for_input(input_, p=False):
    p1 = part_one(input_)
    p2 = part_two(input_, p=p)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 8)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_, p=True)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

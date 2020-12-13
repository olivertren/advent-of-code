import datetime
from functools import reduce

from utils import get_input, print_answers


def part_one(i):
    time = int(i[0])
    id_ = i[1].split(",")
    id_ = [int(i) for i in id_ if i != "x"]

    min_ = 1000000000000
    c = 0
    for t in id_:
        r = -time % t
        if r < min_:
            min_ = r
            c = t * r
    return c


def part_two(i):
    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a * b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod

    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    id_ = i[1].split(",")
    id_s = []
    for i in id_:
        if i == "x":
            id_s.append(i)
        else:
            id_s.append(int(i))

    r = {i: id_s.index(i) for i in [int(j) for j in id_ if j != "x"]}

    n = []
    a = []
    for i, j in r.items():
        n.append(i)
        a.append(i - j)

    return chinese_remainder(n, a)


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

import datetime
from collections import Counter

from utils import get_input, print_answers

e = "L"
o = "#"
f = "."
a = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def solution(i, transform_seat):
    def one_pass(i):
        updates = {}
        for r, c in i.keys():
            updates[(r, c)] = transform_seat(i, r, c)

        return updates

    new = one_pass(i)
    while new != i:
        i = new
        new = one_pass(i)

    return Counter(new.values()).get(o)


def part_one(i):
    def transform_seat(i, r, c):
        def a_seats(r, c):
            count = 0
            for _r, _c in a:
                if i.get((r + _r, c + _c)) == o:
                    count += 1
            return count

        if i.get((r, c)) == e and a_seats(r, c) == 0:
            return o
        elif i.get((r, c)) == o and a_seats(r, c) >= 4:
            return e
        return i.get((r, c))

    return solution(i, transform_seat)


def part_two(i):
    def transform_seat(i, r, c):
        def a_seats(r, c):
            count = 0
            for _r, _c in a:
                __r = r + _r
                __c = c + _c
                s = i.get((__r, __c))
                while s is not None and s == f:
                    __r = __r + _r
                    __c = __c + _c
                    s = i.get((__r, __c))
                if s == o:
                    count += 1

            return count

        if i.get((r, c)) == e and a_seats(r, c) == 0:
            return o
        elif i.get((r, c)) == o and a_seats(r, c) >= 5:
            return e
        return i.get((r, c))

    return solution(i, transform_seat)


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


def get_seats(input_):
    seats = {}
    for i in range(len(input_)):
        for j in range(len(input_[i])):
            seats[(i, j)] = input_[i][j]
    return seats


input_ = get_input(f"2020/day{datetime.date.today().day}test")
print("Tests")
print_answers_for_input(get_seats(input_))

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(get_seats(input_))

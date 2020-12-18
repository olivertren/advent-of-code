import itertools

from utils import get_input, print_answers

A = "#"
I = "."


def get_range(i_, c):
    is_ = set(map(lambda k: k[i_], c.keys()))
    return range(min(is_) - 1, max(is_) + 2)


def part_one(i_):
    c = {}
    for x, l in enumerate(i_):
        for y, p in enumerate(l):
            c[(x, y, 0)] = p

    def adj(x, y, z, c):
        count = 0
        n = [-1, 0, 1]
        for (i, j, k) in itertools.product(n, n, n):
            if i == j == k == 0:
                continue
            else:
                try:
                    if c[(x + i, y + j, z + k)] == A:
                        count += 1
                except KeyError:
                    pass

        return count

    def update(c):
        c_ = {}
        xs = get_range(0, c)
        ys = get_range(1, c)
        zs = get_range(2, c)

        for x, y, z in itertools.product(xs, ys, zs):
            adj_count = adj(x, y, z, c)
            try:
                p = c[(x, y, z)]
            except KeyError:
                p = I
            if p == A:
                if 2 <= adj_count <= 3:
                    c_[(x, y, z)] = A
                else:
                    c_[(x, y, z)] = I
            else:
                if adj_count == 3:
                    c_[(x, y, z)] = A
                else:
                    c_[(x, y, z)] = I

        return c_

    for i in range(6):
        c = update(c)

    return len([k for k, v in c.items() if v == A])


def part_two(i_):
    c = {}
    for x, l in enumerate(i_):
        for y, p in enumerate(l):
            c[(x, y, 0, 0)] = p

    def adj(x, y, z, w, c):
        count = 0
        n = [-1, 0, 1]
        for i, j, k, l in itertools.product(n, n, n, n):
            if i == j == k == l == 0:
                continue
            else:
                try:
                    if c[(x + i, y + j, z + k, w + l)] == A:
                        count += 1
                except KeyError:
                    pass

        return count

    def update(c):
        c_ = {}
        xs = get_range(0, c)
        ys = get_range(1, c)
        zs = get_range(2, c)
        ws = get_range(3, c)

        for x, y, z, w in itertools.product(xs, ys, zs, ws):
            adj_count = adj(x, y, z, w, c)
            try:
                p = c[(x, y, z, w)]
            except KeyError:
                p = I
            if p == A:
                if 2 <= adj_count <= 3:
                    c_[(x, y, z, w)] = A
                else:
                    c_[(x, y, z, w)] = I
            else:
                if adj_count == 3:
                    c_[(x, y, z, w)] = A
                else:
                    c_[(x, y, z, w)] = I

        return c_

    for i in range(6):
        c = update(c)

    return len([k for k, v in c.items() if v == A])


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day17test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

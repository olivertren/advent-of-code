import datetime

import tqdm

from utils import get_groups, print_answers


def parse(ns):
    alg, img = ns
    alg = "".join(alg.split("\n"))
    alg = alg.replace(".", "0")
    alg = alg.replace("#", "1")
    img = img.split("\n")
    img_set = set()

    for i, row in enumerate(img):
        for j, p in enumerate(row):
            if p == ".":
                pass
            elif p == "#":
                img_set.add((i, j))
            else:
                raise Exception("Parse Error")

    return alg, img_set


def get_neighbors(x, y, img):
    xs = {i[0] for i in img}
    ys = {i[1] for i in img}
    max_x = max(xs)
    min_x = min(xs)
    max_y = max(ys)
    min_y = min(ys)

    n = []
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if x + i > max_x or x + i < min_x or y + j > max_y or y + j < min_y:
            n.append(None)
        else:
            n.append((x + i, y + j))
    return n


def enhance(x, y, img, alg, outside, min_x, max_x, min_y, max_y):
    b = ""
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if x + i > max_x or x + i < min_x or y + j > max_y or y + j < min_y:
            b += outside
        elif (x + i, y + j) in img:
            b += "1"
        else:
            b += "0"
    return alg[int(b, 2)]


def iterate(img, alg, outside):
    xs = {i[0] for i in img}
    ys = {i[1] for i in img}
    max_x = max(xs)
    min_x = min(xs)
    max_y = max(ys)
    min_y = min(ys)

    img_set = set()

    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            p = enhance(x, y, img, alg, outside, min_x, max_x, min_y, max_y)
            if p == "1":
                img_set.add((x, y))

    return img_set


def part_one(ns, swap, iters=2):
    alg, img_set = parse(ns)
    for i in tqdm.trange(iters):
        if not swap:
            outside = "0"
        else:
            outside = "0" if i % 2 == 0 else "1"
        img_set = iterate(img_set, alg, outside)
    return len(img_set)


def part_two(ns, swap):
    return part_one(ns, swap, iters=50)


def print_answers_for_input(input_, swap=False):
    p1 = part_one(input_, swap)
    p2 = part_two(input_, swap)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 20)
input_ = get_groups(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_, swap=True)

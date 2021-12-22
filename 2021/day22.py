import datetime

import numpy as np
import tqdm

from utils import get_input, print_answers


def parse(ns):
    ins = []
    for n in ns:
        on, xyz = n.split(" ")
        on = 1 if on == "on" else 0
        x, y, z = xyz.split(",")
        x1, x2 = x.split("=")[1].split("..")
        y1, y2 = y.split("=")[1].split("..")
        z1, z2 = z.split("=")[1].split("..")
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        z1 = int(z1)
        z2 = int(z2)
        ins.append([on, [x1, x2], [y1, y2], [z1, z2]])
    return ins


def part_one(ns):
    ins = parse(ns)
    c = np.zeros((101, 101, 101))
    for on, x, y, z in ins:
        x1, x2 = np.array(x) + 50
        y1, y2 = np.array(y) + 50
        z1, z2 = np.array(z) + 50
        if x1 < 0 or x2 > 100 or y1 < 0 or y2 > 100 or z1 < 0 or z2 > 100:
            continue
        else:
            c[x1 : x2 + 1, y1 : y2 + 1, z1 : z2 + 1] = on
    return int(np.sum(c))


def get_overlap(x1, y1, z1, x2, y2, z2):
    min_x = max(x1[0], x2[0])
    max_x = min(x1[1], x2[1])

    min_y = max(y1[0], y2[0])
    max_y = min(y1[1], y2[1])

    min_z = max(z1[0], z2[0])
    max_z = min(z1[1], z2[1])

    if (min_x > max_x) or (min_y > max_y) or (min_z > max_z):
        return None

    return min_x, max_x, min_y, max_y, min_z, max_z


def update_cubes(cubes, on, x, y, z, i):
    for k, val in cubes.copy().items():
        min_x, max_x, min_y, max_y, min_z, max_z, d = k
        rx = [min_x, max_x]
        ry = [min_y, max_y]
        rz = [min_z, max_z]

        overlap = get_overlap(x, y, z, rx, ry, rz)
        if overlap is None:
            continue
        else:
            min_x, max_x, min_y, max_y, min_z, max_z = overlap
            if (min_x, max_x, min_y, max_y, min_z, max_z, d + i) in cubes:
                raise Exception
            if val == 1:
                cubes[(min_x, max_x, min_y, max_y, min_z, max_z, d + i)] = -1
            else:
                cubes[(min_x, max_x, min_y, max_y, min_z, max_z, d + i)] = 1

    if on == 1:
        cubes[(x[0], x[1], y[0], y[1], z[0], z[1], i)] = 1


def part_two(ns):
    ins = parse(ns)
    cubes = {}
    for i, val in tqdm.tqdm(enumerate(ins)):
        on, x, y, z = val
        update_cubes(cubes, on, x, y, z, str(i))
    return sum(v * (k[1] - k[0] + 1) * (k[3] - k[2] + 1) * (k[5] - k[4] + 1) for k, v in cubes.items())


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 22)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

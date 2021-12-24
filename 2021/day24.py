import datetime
import functools
import json
import math
from collections import defaultdict

from utils import get_input, print_answers

INP = "inp"
ADD = "add"
MUL = "mul"
DIV = "div"
MOD = "mod"
EQL = "eql"
W = "w"
X = "x"
Y = "y"
Z = "z"


def parse(ns):
    raw_insts = [n.split(" ") for n in ns]
    insts = []
    for inst in raw_insts:
        if inst[0] == INP:
            insts.append([])
        insts[-1].append(inst)
    return insts


@functools.lru_cache(maxsize=None)
def iterate(z, insts_block):
    r = {}
    insts_block = json.loads(insts_block)
    for possible_inp in range(1, 10):
        values = {W: 0, X: 0, Y: 0, Z: z}
        for inst in insts_block:
            op = inst[0]
            a_key = inst[1]
            a_val = values[inst[1]]

            if op == INP:
                values[a_key] = possible_inp
            else:
                b = inst[2]
                try:
                    b = int(b)
                except Exception:
                    b = values[b]
                if inst[0] == ADD:
                    values[inst[1]] = values[inst[1]] + b
                elif inst[0] == MUL:
                    values[inst[1]] = values[inst[1]] * b
                elif inst[0] == DIV:
                    if b == 0:
                        raise Exception
                    values[inst[1]] = values[inst[1]] // b if b > 0 else math.ceil(values[inst[1]] / b)
                elif inst[0] == MOD:
                    if a_val < 0 or b <= 0:
                        raise Exception
                    values[inst[1]] = values[inst[1]] % b
                elif inst[0] == EQL:
                    values[inst[1]] = int(values[inst[1]] == b)
                else:
                    raise Exception
            r[possible_inp] = values
    return r


def part_one(ns, comp=">"):
    insts = parse(ns)
    possible_values = defaultdict(dict)
    possible_values[-1] = {0: ""}

    for i in range(14):
        for v, p in possible_values[i - 1].items():
            r = iterate(v, json.dumps(insts[i]))
            for k, new_v in r.items():
                z = new_v[Z]
                if z in possible_values[i]:
                    # the only difference between parts 1 and part 2
                    if comp == ">":
                        if int(str(p) + str(k)) > int(possible_values[i][z]):
                            possible_values[i][z] = str(p) + str(k)
                    elif comp == "<":
                        if int(str(p) + str(k)) < int(possible_values[i][z]):
                            possible_values[i][z] = str(p) + str(k)
                    else:
                        raise Exception(f"comp {comp} is invalid")
                else:
                    possible_values[i][z] = str(p) + str(k)

        min_v = min(possible_values[i].keys())
        for v in list(possible_values[i].keys()):
            if v > min_v * 10:
                del possible_values[i][v]
    return possible_values[13][0]


def part_two(ns):
    return part_one(ns, "<")


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 24)
input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

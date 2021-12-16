import datetime
from functools import reduce
from operator import mul

from utils import get_input, print_answers


def parse(h, num_packets=None):
    packets = []
    while "1" in h:
        if num_packets is not None and len(packets) == num_packets:
            break
        version, type_, h = h[:3], h[3:6], h[6:]
        version = int(version, 2)
        type_ = int(type_, 2)
        if type_ == 4:
            five, h = h[:5], h[5:]
            lit = ""
            while five[0] == "1":
                lit += five[1:]
                five, h = h[:5], h[5:]
            # five[0] == '0'
            lit += five[1:]
            packets.append((version, type_, int(lit, 2)))
        else:
            len_id, h = h[:1], h[1:]
            if len_id == "0":
                sub_h, h = h[:15], h[15:]
                sub_h = int(sub_h, 2)
                sub_h, h = h[:sub_h], h[sub_h:]
                sub_packets, _ = parse(sub_h)
                packets.append((version, type_, sub_packets))
            else:  # len_id == "1"
                sub_h, h = h[:11], h[11:]
                sub_h = int(sub_h, 2)
                sub_packets, h = parse(h, num=sub_h)
                packets.append((version, type_, sub_packets))
    return packets, h


def get_scores(packets):
    score = 0
    for v, t, p in packets:
        score += v
        if isinstance(p, list):
            score += get_scores(p)
    return score


def part_one(ns):
    output = "\n"
    for n in ns:
        num_bits = len(n) * 4
        h = bin(int(n, 16))[2:].zfill(num_bits)
        packets, h = parse(h)
        output += str(get_scores(packets)) + "\n"
    return output


def evaulate(packets):
    val = []
    for v, t, p in packets:
        if isinstance(p, list):
            p = evaulate(p)
        if t == 4:
            val.append(p)
        elif t == 0:
            val.append(sum(p))
        elif t == 1:
            val.append(reduce(mul, p, 1))
        elif t == 2:
            val.append(min(p))
        elif t == 3:
            val.append(max(p))
        elif t == 5:
            val.append(int(p[0] > p[1]))
        elif t == 6:
            val.append(int(p[0] < p[1]))
        elif t == 7:
            val.append(int(p[0] == p[1]))
    return val


def part_two(ns):
    output = "\n"
    for n in ns:
        num_bits = len(n) * 4
        h = bin(int(n, 16))[2:].zfill(num_bits)
        packets, h = parse(h)
        output += str(evaulate(packets)[0]) + "\n"
    return output


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 16)
input_ = get_input(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

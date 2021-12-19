import datetime
import itertools
import json
import math
from collections import deque
from functools import cached_property, lru_cache

from scipy.spatial.distance import cityblock

from utils import get_groups, print_answers


class Scanner:
    def __init__(self, points, location=(0, 0, 0)):
        self.points = points
        self.location = location

    @classmethod
    def scanner_from_input(cls, ns):
        lines = ns.split("\n")[1:]
        points = [n.split(",") for n in lines]
        points = [(int(x), int(y), int(z)) for x, y, z in points]
        return cls(points)

    @cached_property
    def pairwise_distances(self):
        return {(p1, p2): math.dist(p1, p2) for p1, p2 in itertools.combinations(self.points, 2)}

    @cached_property
    def pairwise_distances_by_point(self):
        return {p1: [math.dist(p1, p2) for p2 in self.points if p1 != p2] for p1 in self.points}

    def __repr__(self):
        return str(self.points)


def find_matching_points(p, dists, s2):
    matching_points = None
    for p2, dists2 in s2.pairwise_distances_by_point.items():
        overlapping_distances = []
        for d in dists:
            if d in dists2:
                overlapping_distances.append(d)

        if len(overlapping_distances) >= 12 - 1:
            return p, p2
    return matching_points


@lru_cache
def find_overlapping_points(s1, s2):
    matching_points = []
    for p, dists in s1.pairwise_distances_by_point.items():
        if mp := find_matching_points(p, dists, s2):
            matching_points.append(mp)
    return matching_points


def reorient_scanner(s1, s2):
    overlapping_points = find_overlapping_points(s1, s2)

    s1_points = [p[0] for p in overlapping_points]
    s1_x = [p[0] for p in s1_points]
    s1_y = [p[1] for p in s1_points]
    s1_z = [p[2] for p in s1_points]
    s2_points = [p[1] for p in overlapping_points]
    s2_x = [p[0] for p in s2_points]
    s2_y = [p[1] for p in s2_points]
    s2_z = [p[2] for p in s2_points]

    s1_x_distances = [abs(p1 - p2) for p1, p2 in itertools.combinations(s1_x, 2)]
    s1_y_distances = [abs(p1 - p2) for p1, p2 in itertools.combinations(s1_y, 2)]
    s1_z_distances = [abs(p1 - p2) for p1, p2 in itertools.combinations(s1_z, 2)]

    s2_x_distances = [abs(p1 - p2) for p1, p2 in itertools.combinations(s2_x, 2)]
    s2_y_distances = [abs(p1 - p2) for p1, p2 in itertools.combinations(s2_y, 2)]
    s2_z_distances = [abs(p1 - p2) for p1, p2 in itertools.combinations(s2_z, 2)]

    # which index corresponds to [x, y, z] axis
    s2_orientation = []
    if s1_x_distances == s2_x_distances:
        s2_orientation.append(0)
    elif s1_x_distances == s2_y_distances:
        s2_orientation.append(1)
    elif s1_x_distances == s2_z_distances:
        s2_orientation.append(2)

    if s1_y_distances == s2_x_distances:
        s2_orientation.append(0)
    elif s1_y_distances == s2_y_distances:
        s2_orientation.append(1)
    elif s1_y_distances == s2_z_distances:
        s2_orientation.append(2)

    if s1_z_distances == s2_x_distances:
        s2_orientation.append(0)
    elif s1_z_distances == s2_y_distances:
        s2_orientation.append(1)
    elif s1_z_distances == s2_z_distances:
        s2_orientation.append(2)

    s2_points = [tuple(p[s2_orientation[i]] for i in range(3)) for p in s2.points]
    s2_location = tuple(s2.location[s2_orientation[i]] for i in range(3))

    overlapping_points = find_overlapping_points(s1, Scanner(s2_points, s2_location))
    s1_point1 = overlapping_points[0][0]
    s1_point2 = overlapping_points[1][0]
    s2_point1 = overlapping_points[0][1]
    s2_point2 = overlapping_points[1][1]
    s2_flips = [1 if (s1_point1[i] > s1_point2[i]) == (s2_point1[i] > s2_point2[i]) else -1 for i in range(3)]
    s2_points = [tuple(s2_flips[i] * p[i] for i in range(3)) for p in s2_points]
    s2_location = tuple(s2_flips[i] * s2.location[i] for i in range(3))

    overlapping_points = find_overlapping_points(s1, Scanner(s2_points, s2_location))
    s1_point = overlapping_points[0][0]
    s2_point = overlapping_points[0][1]
    s2_translation = [s1_point[i] - s2_point[i] for i in range(3)]
    s2_points = [tuple(p[i] + s2_translation[i] for i in range(3)) for p in s2_points]
    s2_location = tuple(s2.location[i] + s2_translation[i] for i in range(3))

    s2 = Scanner(s2_points, s2_location)
    assert len(set(s1.points).intersection(set(s2.points))) == 12

    return s2


@lru_cache
def get_scanners(ns):
    ns = json.loads(ns)
    scanners = [Scanner.scanner_from_input(n) for n in ns]
    num_scanners = len(scanners)
    overlapping_scanners = deque()
    seen_scanners = {0}

    for i in range(num_scanners):
        for j in range(num_scanners):
            if i >= j:
                continue
            if find_overlapping_points(scanners[i], scanners[j]):
                overlapping_scanners.append((i, j))

    while overlapping_scanners:
        i, j = overlapping_scanners.popleft()
        if i in seen_scanners and j in seen_scanners:
            continue
        if i in seen_scanners:
            scanners[j] = reorient_scanner(scanners[i], scanners[j])
            seen_scanners.add(j)
            continue
        if j in seen_scanners:
            scanners[i] = reorient_scanner(scanners[j], scanners[i])
            seen_scanners.add(i)
            continue
        overlapping_scanners.append((i, j))

    return scanners


def part_one(ns):
    scanners = get_scanners(json.dumps(ns))

    seen_points = set()
    for sc in scanners:
        seen_points.update(sc.points)

    return len(seen_points)


def part_two(ns):
    scanners = get_scanners(json.dumps(ns))
    max_dist = 0

    for sc1, sc2 in itertools.combinations(scanners, 2):
        if (dist := cityblock(sc1.location, sc2.location)) > max_dist:
            max_dist = dist

    return max_dist


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


today = datetime.date(2021, 12, 19)
input_ = get_groups(f"{today.year}/day{today.day}test")
print("Tests")
print_answers_for_input(input_)

input_ = get_groups(__file__)
print("Actual")
print_answers_for_input(input_)

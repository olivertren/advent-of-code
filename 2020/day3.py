from functools import reduce
from operator import mul

from utils import get_input, print_answers


def num_trees(tree_map, down, right):
    return sum([1 for i in range(len(tree_map) // down) if tree_map[down * i][right * i % len(tree_map[0])] == "#"])


tree_map = get_input(__file__)
print_answers(
    num_trees(tree_map, 1, 3),
    reduce(
        mul,
        [num_trees(tree_map, down, right) for down, right in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]],
    ),
)

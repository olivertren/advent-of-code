from utils import get_input, print_answers


def part_one(i_):
    cups = [int(_) for _ in i_[0]]
    for i in range(100):
        current = cups[0]
        next_three = cups[1:4]
        left_over_cups = cups[4:]

        smaller_cups = {c for c in left_over_cups if c < current}
        larger_cups = set(left_over_cups) - smaller_cups
        if smaller_cups:
            dest_cup = max(smaller_cups)
        else:
            dest_cup = max(larger_cups)

        dest_idx = left_over_cups.index(dest_cup)

        cups = left_over_cups[: dest_idx + 1] + next_three + left_over_cups[dest_idx + 1 :] + [current]

    return "".join([str(i) for i in cups[1:]])


class Node:
    next: "Node"

    def __init__(self, value):
        self.value = value


def part_two(i_):
    cups = [int(_) for _ in i_[0]]
    cups += list(range(10, 1_000_000 + 1))

    current = node_zero = Node(cups[0])
    nodes = {current.value: node_zero}
    for i in cups[1:]:
        next_ = Node(i)
        nodes[i] = next_
        current.next = next_
        current = next_
    current.next = node_zero

    current = node_zero

    def get_dest_node(current, pickup):
        value = current.value
        picked_up_values = {p.value for p in pickup}

        dest_node = value - 1
        if dest_node == 0:
            dest_node = 1_000_000
        while dest_node in picked_up_values:
            dest_node -= 1
            if dest_node == 0:
                dest_node = 1_000_000
        return dest_node

    for _ in range(10_000_000):
        pickup = [current.next, current.next.next, current.next.next.next]
        current.next = current.next.next.next.next

        dest_node = nodes[get_dest_node(current, pickup)]
        dest_node.next, pickup[-1].next = pickup[0], dest_node.next
        current = current.next

    return nodes[1].next.value * nodes[1].next.next.value


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day23test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

from utils import get_input, print_answers

P = "+"
M = "*"

LP = "("
RP = ")"


def get_vals(equation):
    _equation = ""
    for i in equation:
        _equation += i
        _equation += " "
    _equation = _equation.lstrip().rstrip()

    vals = _equation.split(" ")
    _vals = []
    for v in vals:
        if v != "":
            _vals.append(v)

    return _vals


def eval_from_list(vals, no_paren):
    if len(vals) == 0:
        return 0

    try:
        lp = vals.index(LP)

        left_operator_idx = lp - 1
        if left_operator_idx < 0:
            left_vals = [0]
            operator = P
        else:
            left_vals = vals[:left_operator_idx]
            operator = vals[left_operator_idx]

        lp_count = 0
        rp_count = 0
        for i, j in enumerate(vals[lp:]):
            if j == LP:
                lp_count += 1
            elif j == RP:
                rp_count += 1
            if lp_count == rp_count:
                rp = lp + i
                break

        paren_value = eval_from_list(vals[lp + 1 : rp], no_paren)

        try:
            vals = [paren_value] + vals[rp + 1 :]
        except IndexError:
            pass

        vals = left_vals + [operator] + vals
        value = eval_from_list(vals, no_paren)

    except ValueError:
        value = no_paren(vals)

    return value


def evaluate(equation):
    vals = get_vals(equation)
    return eval_from_list(vals, no_paren1)


def no_paren1(vals):
    current = int(vals[0])
    vals = vals[1:]

    for i in vals:
        if i == P:
            operator = P
        elif i == M:
            operator = M
        elif operator == P:
            current += int(i)
        else:
            current *= int(i)

    return current


def part_one(i_):
    sum_ = 0
    for e in i_:
        sum_ += evaluate(e)

    return sum_


def no_paren2(vals):
    while P in vals:
        _vals = vals.copy()
        p_idx = vals.index(P)
        vals = vals[: p_idx - 1] + [int(vals[p_idx - 1]) + int(vals[p_idx + 1])]
        try:
            vals = vals + _vals[p_idx + 2 :]
        except IndexError:
            pass

    value = 1
    for v in vals:
        if v != M:
            value *= int(v)

    return value


def evaluate2(equation):
    vals = get_vals(equation)
    return eval_from_list(vals, no_paren2)


def part_two(i_):
    sum_ = 0
    for e in i_:
        sum_ += evaluate2(e)

    return sum_


def print_answers_for_input(input_):
    p1 = part_one(input_)
    p2 = part_two(input_)

    print_answers(p1, p2)


input_ = get_input(f"2020/day18test")
print("Tests")
print_answers_for_input(input_)

input_ = get_input(__file__)
print("Actual")
print_answers_for_input(input_)

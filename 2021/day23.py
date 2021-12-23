import functools
import json
import time
from copy import deepcopy as cp

A = "A"
B = "B"
C = "C"
D = "D"

letter_to_square = {A: 2, B: 4, C: 6, D: 8}
square_to_letter = {
    2: A,
    4: B,
    6: C,
    8: D,
}
letter_to_score = {
    A: 1,
    B: 10,
    C: 100,
    D: 1000,
}
non_letter_idx = set(range(11)) - set(letter_to_square.values())


@functools.lru_cache(maxsize=None)
def get_min_score(p_, finish_, max_letters_per_bucket):
    p__ = json.loads(p_)
    finish = json.loads(finish_)
    if p__ == finish:
        return [], "", 0, 0

    next_ps = []
    for i, square in enumerate(p__):
        p_copy = cp(p__)
        if len(square) == 0:
            continue

        if i in square_to_letter.keys() and all(c == square_to_letter[i] for c in square):
            continue

        if i in non_letter_idx:
            cur = p_copy[i].pop(0)
            s = letter_to_square[cur]
            if all(c == cur for c in p_copy[s]):
                if any(len(p_copy[j]) != 0 for j in non_letter_idx if s > j > i):
                    continue
                if any(len(p_copy[j]) != 0 for j in non_letter_idx if i > j > s):
                    continue
                score_ = letter_to_score[cur] * (abs(s - i) + max_letters_per_bucket - len(p_copy[s]))
                p_copy[s].append(cur)
                min_score_ = get_min_score(json.dumps(p_copy), json.dumps(finish), max_letters_per_bucket)
                if min_score_ is None:
                    continue

                next_ps.append((p_copy, f"{cur} {i} -> {s}", score_, score_ + min_score_[3]))

        if i in square_to_letter.keys():
            cur = p_copy[i].pop(0)
            pop_score = (max_letters_per_bucket - len(p_copy[i])) * letter_to_score[cur]
            for j in non_letter_idx:
                if any(len(p_copy[k]) != 0 for k in non_letter_idx if i > k > j):
                    continue
                if any(len(p_copy[k]) != 0 for k in non_letter_idx if j > k > i):
                    continue
                if len(p_copy[j]) == 1:
                    continue
                p_copy_copy = cp(p_copy)
                p_copy_copy[j].append(cur)
                score_ = pop_score + letter_to_score[cur] * (abs(j - i))
                min_score_ = get_min_score(json.dumps(p_copy_copy), json.dumps(finish), max_letters_per_bucket)
                if min_score_ is None:
                    continue

                next_ps.append(
                    (
                        p_copy_copy,
                        f"{cur} {i} -> {j}",
                        score_,
                        score_ + min_score_[3],
                    )
                )

    if len(next_ps) == 0:
        return None

    return min(next_ps, key=lambda x: x[3])


def run(p, finish, max_letters_per_bucket):
    start = time.time()
    p_ = p
    get_min_score(json.dumps(p_), json.dumps(finish), max_letters_per_bucket)
    print(time.time() - start)
    while p_:
        next_p_, move, score_, min_score_ = get_min_score(json.dumps(p_), json.dumps(finish), max_letters_per_bucket)
        print(f"{min_score_}\t{p_}\t{move}\t{score_}")
        p_ = next_p_


p_start = [[], [], [C, B], [], [A, A], [], [B, D], [], [D, C], [], []]
FINISH = [[], [], [A, A], [], [B, B], [], [C, C], [], [D, D], [], []]
MAX_LETTERS_PER_BUCKET = 2
run(p_start, FINISH, MAX_LETTERS_PER_BUCKET)


p_start = [
    [],
    [],
    [C, D, D, B],
    [],
    [A, C, B, A],
    [],
    [B, B, A, D],
    [],
    [D, A, C, C],
    [],
    [],
]
FINISH = [
    [],
    [],
    [A, A, A, A],
    [],
    [B, B, B, B],
    [],
    [C, C, C, C],
    [],
    [D, D, D, D],
    [],
    [],
]
MAX_LETTERS_PER_BUCKET = 4
run(p_start, FINISH, MAX_LETTERS_PER_BUCKET)

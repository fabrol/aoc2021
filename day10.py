from collections import defaultdict
from typing import Counter, List, Tuple
import logging
import sys
import itertools
logging.basicConfig(stream=sys.stderr, level=logging.INFO)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


CLOSE_TO_OPEN_ = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

OPEN_TO_CLOSE_ = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def get_line_score(line):
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            if stack[-1] == CLOSE_TO_OPEN_[c]:
                stack.pop()
            else:
                # Found a mismatch
                return SCORES[c]
    return 0


def run_part_a(lines):
    return sum([get_line_score(l.strip()) for l in lines])


def get_completion_score(line):
    stack = []
    for c in line:
        if c in ['(', '[', '{', '<']:
            stack.append(c)
        else:
            if stack[-1] == CLOSE_TO_OPEN_[c]:
                stack.pop()
            else:
                raise ("Wtf")

    # Stack should have unmatched
    to_match = list(reversed([OPEN_TO_CLOSE_[x] for x in stack]))
    logging.debug(f'For {line} matching with: {"".join(to_match)}')

    score = 0
    for v in to_match:
        score = ((score * 5) + POINTS[v])
        logging.debug(f'{v} {POINTS[v]} {score}')

    logging.debug(f'Line {line}, score: {score}')
    return score


def run_part_b(lines):
    scores = []
    for l in lines:
        if get_line_score(l) != 0:
            continue
        else:
            scores.append(get_completion_score(l))
    return sorted(scores)[int(len(scores)/2)]


def test_part_a():
    expected = 26397
    actual = run_part_a(read_input('test10.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 288957
    actual = run_part_b(read_input('test10.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_a()
print(f"Part A: {run_part_a(read_input('day10.in'))}")

test_part_b()
print(f"Part B: {run_part_b(read_input('day10.in'))}")

from collections import defaultdict
from email.policy import default
import re
from typing import Counter, List, Tuple
import logging
import sys
import itertools
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def run_part_a(lines, iters):
    template = list(lines[0])
    mappings = lines[2:]
    mapping = {}
    for i in range(len(mappings)):
        frm, to = re.match('(\D+) -> (\D)', mappings[i]).groups()
        mapping[frm] = to
    bi_mapping = {}
    for bigram, to in mapping.items():
        bi_mapping[bigram] = [
            ''.join([bigram[0], to]), ''.join([to, bigram[1]])]

    print(template)
    pairs = defaultdict(int)  # bigram -> N
    count = Counter(template)
    print(count)
    for i, ch in enumerate(template[:-1]):
        bigram = ''.join(template[i:i+2])
        pairs[bigram] += 1

    for step in range(iters):
        for p, val in list(pairs.items()):
            if p in bi_mapping:
                to1, to2 = bi_mapping[p]
                pairs[to1] += val
                pairs[to2] += val
                pairs[p] -= val
                count.update({mapping[p]: val})
                #print(f"Updating {p} from {pairs} cur: {count}")

        print(f"Step {step} setup {count}")

    print(count)
    return count.most_common()[0][1] - count.most_common()[-1][1]


def run_part_b(lines):
    pass


def test_part_a():
    expected = 1588
    actual = run_part_a(read_input('test14.in'), 10)

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 2188189693529
    actual = run_part_a(read_input('test14.in'), 40)

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_a()
print(f"Part A: {run_part_a(read_input('day14.in'), 10)}")

test_part_b()
print(f"Part B: {run_part_a(read_input('day14.in'), 40)}")

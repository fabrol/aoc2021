from collections import defaultdict
from typing import Counter, List, Tuple
import logging
import sys
import itertools
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def run_part_a(lines):
    total = 0
    acceptable_lens = set([2, 3, 4, 7])
    for line in lines:
        inputs_str, outputs_str = line.split("|")
        digits = outputs_str.strip().split(" ")
        for d in digits:
            if len(d) in acceptable_lens:
                total += 1

    return total


def sort_list(digit_strs):
    return ["".join(sorted(d)) for d in digit_strs]


def get_mapping(inputs_strs):
    out = [None] * 7   # word, index == segment index

    # dab=7, ab=1 --> d is Top (a and b are either of TR BR)
    # eafb: 4 --> e and f are either of TL or C
    # 9 - 4 = cefabd - eafb = c -> c is B
    # 5 = cdfbe - Top (d) - bottom (c) = fbe  - {TL or C from 4} {f, e} = b -> b = BR
    # (7 & 1) {TR or BR} (a and b) - BR (b) --> a is TR
    # 3 - (top, bottom, BR, TR) = center
    # 4 - (center, TR, BR) = TL
    # abcdefg - known letters = BL

    for s in inputs_strs:
        if len(s) == 2:
            out[1] = s
        elif len(s) == 3:
            out[7] = s
        elif len(s) == 4:
            out[4] = s
        elif len(s) == 7:
            out[8] = s
    # Diff out[7] and out[1]
    # Diff

    return out


"""
 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
"""


def to_mapping(p):
    # abcdefg
    # 0123456

    # sorted(p[0] + p[1]) -> 1
    # (0,1) -> 1
    index_to_val = {
        (0, 1, 2, 3, 4, 6): 0,
        (0, 1): 1,
        (3, 0, 5, 6, 2): 2,
        (0, 1, 3, 5, 2): 3,
        (4, 5, 0, 1): 4,
        (3, 4, 5, 1, 2): 5,
        (1, 2, 3, 4, 5, 6): 6,
        (0, 1, 3): 7,
        (0, 1, 2, 3, 4, 5, 6): 8,
        (0, 1, 2, 3, 4, 5): 9,
    }
    out = [None]*10
    for ind, val in index_to_val.items():
        w = "".join(sorted([p[i] for i in ind]))
        out[val] = w
    return out


def generate_segments():
    return itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g'])


def get_mapping_bf(inputs_strs):
    input_str_set = set(inputs_strs)

    for p in generate_segments():
        # p = 'cdgfeba' -> 1-7 mapping
        p_inputs = to_mapping(p)
        p_input_set = set(p_inputs)
        if input_str_set == p_input_set:
            return p_inputs
    print('fuck')
    return None


def run_part_b(lines):
    total = 0
    for line in lines:
        inputs_raw, outputs_raw = line.split("|")
        output_strs = sort_list(outputs_raw.strip().split(' '))
        inputs_strs = sort_list(inputs_raw.strip().split(' '))

        mapping = get_mapping_bf(inputs_strs)
        num_list = [mapping.index(outs) for outs in output_strs]
        num = int("".join([str(n) for n in num_list]))
        total += num

    return total


def test_part_b():
    expected = 5353
    line = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    actual = run_part_b(line)

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_b()
print(f"Part B: {run_part_b(read_input('day8.in'))}")

"""
:
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc

So, the unique signal patterns would correspond to the following digits:

    ab: 1
    dab: 7
    eafb: 4
    cdfbe: 5
    gcdfa: 2
    fbcad: 3
    cefabd: 9
    cdfgeb: 6
    cagedb: 0
    acedgfb: 8

  T
TL  TR
  C 
BL  BR
  B

dab - ab = 7 - 1: d is Top and (a,b)==(TR,BR)
eafb - ab = 4 - 1: (e,f)==(TL,C)
dab - eafb = 7 - 4: (no new info)
acedgfb - eafb: 8 - 4: (c,d,g)==(T,BL,B)


abcdef: 9 # g
bcdefg: 6 # a
abcdeg: 0 # f
(g,a,f) == (TR, C, BL)

cdfbe: 5  # a, g
gcdfa: 2  # 
fbcad: 3
()






dab=7, ab=1 --> d is Top (a and b are either of TR BR)
eafb: 4 --> e and f are either of TL or C
9 - 4 = cefabd - eafb = c -> c is B
5 = cdfbe - Top (d) - bottom (c) = fbe  - {TL or C from 4} {f, e} = b -> b = BR
(7 & 1) {TR or BR} (a and b) - BR (b) --> a is TR
3 - (top, bottom, BR, TR) = center
4 - (center, TR, BR) = TL
abcdefg - known letters = BL

Known: Top, Bottom, BR, TR, center, TL





"""

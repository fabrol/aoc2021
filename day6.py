from collections import defaultdict
from typing import Counter, List, Tuple
from dataclasses import dataclass
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def run(initial_fish, itr) -> int:
    fish_counters = [0]*9
    for x in initial_fish[0].split(','):
        fish_counters[int(x)] += 1

    for i in range(itr):
        new_fish = fish_counters[0]
        fish_counters[0:8] = fish_counters[1:]
        fish_counters[6] += new_fish
        fish_counters[8] = new_fish

    return sum(fish_counters)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def test_part_a():
    expected = 5934
    actual = run(["3,4,3,1,2"], 80)

    assert actual == expected, f'Actual {actual} expected {expected}'


def test_part_b():
    expected = 26984457539
    actual = run(["3,4,3,1,2"], 256)

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_b()
print(f'Part B: {run(read_input("day6.in"), 256)}')

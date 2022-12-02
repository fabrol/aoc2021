from collections import defaultdict
from typing import List, Tuple, Set
import logging
import sys
import itertools
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def dfs(g, node, path_so_far: List, paths: Set):

    if node == ''
    pass


def run_part_a(lines):
    graph = defaultdict(list)
    for l in lines:
        source, target = l.split('-')
        graph[source].append(target)
        graph[target].append(source)
    pass


def run_part_b(lines):
    pass


def test_part_a():
    expected = 5353
    actual = run_part_a(read_input('test12.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 5353
    actual = run_part_b(read_input('test12.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_a()
print(f"Part A: {run_part_a(read_input('day12.in'))}")

test_part_b()
print(f"Part B: {run_part_b(read_input('day12.in'))}")

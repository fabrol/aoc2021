from collections import defaultdict
from io import FileIO
from typing import Counter, List, Tuple
import logging
import sys
import itertools
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def run_part_a(filename):
    fp = open(filename)
    points = []
    while True:
        line = fp.readline()
        if line == "\n":
            break
        points.append(tuple(map(int, line.rstrip().split(','))))

    dir, val = fp.readline().rstrip().split(' ')[-1].split('=')
    val = int(val)

    if dir == 'y':
        maxy = val
        points = list(map(lambda x_y: (x_y[0], val - abs(x_y[1]-val)), points))
    if dir == 'x':
        maxx = val
        points = list(map(lambda x_y: (val - abs(x_y[0]-val), x_y[1]), points))

    return len(set(points))


def run_part_b(filename):
    fp = open(filename)
    points = []
    while True:
        line = fp.readline()
        if line == "\n":
            break
        points.append(tuple(map(int, line.rstrip().split(','))))

    maxx, maxy = -1, -1
    while True:
        line = fp.readline().rstrip()
        if not len(line):
            break
        dir, val = line.rstrip().split(' ')[-1].split('=')
        val = int(val)

        if dir == 'y':
            maxy = val
            points = list(
                map(lambda x_y: (x_y[0], val - abs(x_y[1]-val)), points))
        if dir == 'x':
            maxx = val
            points = list(
                map(lambda x_y: (val - abs(x_y[0]-val), x_y[1]), points))

    print_graph(points, maxx, maxy)
    return len(set(points))


def print_graph(points, max_x, max_y):
    # points = [(x,y),(x1,y1)]
    for y in range(0, max_y):
        for x in range(0, max_x):
            v = '# ' if (x, y) in points else '. '
            print(v, end='')
        print('')


def test_part_a():
    expected = 17
    actual = run_part_a('test13.in')

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 16
    actual = run_part_b('test13.in')

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_a()
print(f"Part A: {run_part_a('day13.in')}")

test_part_b()
print(f"Part B: {run_part_b('day13.in')}")

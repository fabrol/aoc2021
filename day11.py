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


OFFSETS_ = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]


def get_neighbor_indices(x, y, graph):
    y_lim = len(graph)
    x_lim = len(graph[0])
    ret_idx = []
    for off in OFFSETS_:
        x_new = x + off[0]
        y_new = y + off[1]
        if x_new < 0 or x_new >= x_lim or y_new < 0 or y_new >= y_lim:
            continue
        else:
            ret_idx.append((x_new, y_new))
    return ret_idx


def run_step(field) -> Tuple[List[int], int]:
    # Return new field and flashes this step

    new_field = [[x+1 for x in row] for row in field]
    flashes = 0

    flashed_this_step = set()
    while True:
        # Check for any flashers and flash em
        flashed = False
        flashers = set()
        for x in range(len(new_field)):
            for y in range(len(new_field[0])):
                if new_field[x][y] > 9:
                    flashes += 1
                    new_field[x][y] = -1
                    flashed = True
                    flashers.add((x, y))
                    flashed_this_step.add((x, y))
        if not flashed:
            break

        # Increase all the adjacents for flashers
        for (x, y) in flashers:
            neighs = get_neighbor_indices(x, y, new_field)
            for (a, b) in neighs:
                if (a, b) not in flashed_this_step:
                    new_field[a][b] += 1

    # Set flashed cells to 0
    for x in range(len(new_field)):
        for y in range(len(new_field[0])):
            if new_field[x][y] == -1:
                new_field[x][y] = 0

    return new_field, flashes


def print_field(field):
    logging.debug('New iter')
    for row in field:
        logging.debug(''.join([str(x) for x in row]))


def run_part_a(lines, iters=100):
    field = [[int(x) for x in l] for l in lines]
    print_field(field)

    flashes = 0
    for _ in range(iters):
        field, new_flashes = run_step(field)
        print_field(field)
        flashes += new_flashes
    return flashes


def run_part_b(lines, iters=1000):
    field = [[int(x) for x in l] for l in lines]
    print_field(field)

    flashes = 0
    for i in range(iters):
        field, new_flashes = run_step(field)
        if new_flashes == 100:
            return i + 1
        # print_field(field)
        flashes += new_flashes
    return None


def test_part_a():
    expected = 1656
    actual = run_part_a(read_input('test11.in'), 100)

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 195
    actual = run_part_b(read_input('test11.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


# test_part_a()
#print(f"Part A: {run_part_a(read_input('day11.in'), 100)}")
#
test_part_b()
print(f"Part B: {run_part_b(read_input('day11.in'))}")

from collections import defaultdict
import heapq
from typing import Counter, Dict, List, Tuple
import logging
import sys
import itertools
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def process_grid(lines) -> Dict:
    grid = []
    for l in lines:
        grid.append(list(map(int, l)))
    return grid

NEIGHBOR_DELTAS = [-1, 1, -1j, 1j]

def get_neighbors(grid, pt):
    max_x = len(grid)
    max_y = len(grid[0])
    ret = []
    for delta in NEIGHBOR_DELTAS:
        option = pt + delta
        if option.real >= max_x or option.imag >= max_y:
            continue
        ret.append(option)
    return ret 

def run_part_a(lines):
    grid = process_grid(lines)
    start = complex(0, 0)
    goal = complex(len(grid[0]), len(grid))

    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0

    while frontier:
        cost, cur  = heapq.heappop(frontier)

        if cur == goal:
            return cost

        for nb in get_neighbors(grid, cur):
            new_cost = cost + grid[int(cur.real)][int(cur.imag)] # or cost + xxx
            if (nb not in cost_so_far) or (new_cost < cost_so_far[nb]):
                cost_so_far[nb] = new_cost
                came_from[nb] = cur
                heapq.heappush(frontier, (new_cost, nb))


def run_part_b(lines):
    pass


def test_part_a():
    expected = 40
    actual = run_part_a(read_input('test15.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 5353
    actual = run_part_b(read_input('test15.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_a()
print(f"Part A: {run_part_a(read_input('day15.in'))}")

test_part_b()
print(f"Part B: {run_part_b(read_input('day15.in'))}")

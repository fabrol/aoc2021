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


def print_grid(g):
    for row in g:
        logging.debug(''.join(list(map(str, row))))


NEIGHBOR_DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_neighbors(grid, pt):
    max_r = len(grid)
    max_c = len(grid[0])
    ret = []
    for delta in NEIGHBOR_DELTAS:
        option = (pt[0] + delta[0], pt[1] + delta[1])
        if option[0] < 0 or option[0] >= max_c or option[1] < 0 or option[1] >= max_r:
            continue
        ret.append(option)
    return ret


def run_part_a(lines):
    grid = process_grid(lines)
    start = (0, 0)
    goal = (len(grid[0])-1, len(grid)-1)

    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0

    while frontier:
        cost, cur = heapq.heappop(frontier)

        if cur == goal:
            return cost

        for nb in get_neighbors(grid, cur):
            new_cost = cost + grid[cur[0]][cur[1]]
            if (nb not in cost_so_far) or (new_cost < cost_so_far[nb]):
                cost_so_far[nb] = new_cost
                came_from[nb] = cur
                heapq.heappush(frontier, (new_cost, nb))


def get_neighbors_b(grid, pt):
    max_c = len(grid*5)
    max_r = len(grid[0]*5)
    ret = []
    for delta in NEIGHBOR_DELTAS:
        option = (pt[0] + delta[0], pt[1] + delta[1])
        if option[0] < 0 or option[0] >= max_c or option[1] < 0 or option[1] >= max_r:
            continue
        ret.append(option)
    return ret


def get_grid(grid, pt):
    max_c = len(grid[0])
    max_r = len(grid)
    r, c = pt

    base_c = int(c / max_c)
    base_r = int(r / max_r)
    wrap_level = base_c + base_r

    g_idx = (r % max_r, c % max_c)
    g_val = grid[g_idx[0]][g_idx[1]]

    new_val = (g_val + wrap_level) % 9
    if new_val == 0:
        new_val = 9
    return new_val


def print_grid_b(grid, repeats=1, came_from={}):
    max_r = len(grid) * repeats
    max_c = len(grid[0]) * repeats
    print(came_from)
    res = [[-1]*max_c for _ in range(max_r)]
    for r in range(0, max_r):
        for c in range(0, max_c):
            res[r][c] = get_grid(grid, (r, c))
            if (r, c) in came_from:
                res[r][c] = f"\033[91m{res[r][c]}\033[0m"
    print_grid(res)


def run_part_b(lines):
    grid = process_grid(lines)
    start = (0, 0)
    goal = ((len(grid)*5)-1, (len(grid[0])*5)-1)

    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {}
    came_from[start] = None
    cost_so_far = {}
    cost_so_far[start] = 0

    while frontier:
        cost, cur = heapq.heappop(frontier)

        if cur == goal:
            logging.debug(
                f"Found at {goal} : {get_grid(grid, cur)} Total: {cost}")
            break

        for nb in get_neighbors_b(grid, cur):
            new_cost = cost + get_grid(grid, cur)
            if (nb not in cost_so_far) or (new_cost < cost_so_far[nb]):
                cost_so_far[nb] = new_cost
                came_from[nb] = cur
                heapq.heappush(frontier, (new_cost, nb))

    path = [goal]
    while goal != start:
        goal = came_from[goal]
        path.append(goal)

    return (cost, path, grid)


def test_part_a():
    expected = 40
    actual = run_part_a(read_input('test15.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 307
    actual, came_from, grid = run_part_b(read_input('test15.in'))

    print_grid_b(grid, 5, came_from)
    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_a()
print(f"Part A: {run_part_a(read_input('day15.in'))}")

test_part_b()
print(f"Part B: {run_part_b(read_input('day15.in'))}")

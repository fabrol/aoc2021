from collections import defaultdict
from typing import Counter, List, Tuple, Set
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
    #(1, 1),
    (1, 0),
    #(1, -1),
    (0, -1),
    #(-1, -1),
    (-1, 0),
    #(-1, 1),
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


def get_neighbors(x, y, graph):
    idxs = get_neighbor_indices(x, y, graph)
    return [graph[y][x] for (x, y) in idxs]
    y_lim = len(graph)
    x_lim = len(graph[0])
    ret = []
    for off in OFFSETS_:
        x_new = x + off[0]
        y_new = y + off[1]
        if x_new < 0 or x_new >= x_lim or y_new < 0 or y_new >= y_lim:
            continue
        else:
            #print(f'Checking {x_new} {y_new} with limits {x_lim} {y_lim}')
            ret.append(graph[y_new][x_new])
    return ret


def dfs(x, y, visited: Set, graph, out_set: Set):
    if (x, y) in visited:
        return
    if graph[y][x] == 9:
        return

    out_set.add((x, y))
    visited.add((x, y))

    idxs = get_neighbor_indices(x, y, graph)
    for x, y in idxs:
        dfs(x, y, visited, graph, out_set)


def flood_fill(graph):
    basins = []  # array of sets of points
    visited = set()  # visited across all DFS'es

    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if (y, x) in visited:
                continue
            else:
                new_basin = set()
                dfs(x=x, y=y, graph=graph, visited=visited, out_set=new_basin)
                basins.append(new_basin)

    basins_sorted = sorted(basins, key=lambda x: len(x), reverse=True)
    return len(basins_sorted[0]) * len(basins_sorted[1]) * len(basins_sorted[2])


def run_part_a(lines):
    graph = [[int(x) for x in l] for l in lines]
    minimas = []
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            ns = get_neighbors(x, y, graph)
            if graph[y][x] < min(ns):
                minimas.append(graph[y][x])

    return sum([1+x for x in minimas])


def run_part_b(lines):
    graph = [[int(x) for x in l] for l in lines]
    return flood_fill(graph)


def test_part_a():
    expected = 15
    actual = run_part_a(read_input('test9.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


def test_part_b():
    expected = 1134
    actual = run_part_b(read_input('test9.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_a()
print(f"Part A: {run_part_a(read_input('day9.in'))}")


test_part_b()
print(f"Part B: {run_part_b(read_input('day9.in'))}")

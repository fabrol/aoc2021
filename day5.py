from typing import Counter, List, Tuple
from dataclasses import dataclass
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


@dataclass
class Line:
    start: List[int]
    end: List[int]

    def is_straight(self):
        return (self.start[0] == self.end[0]) or (self.start[1] == self.end[1])

    def __hash__(self) -> int:
        return int(''.join(self.start+self.end))

    def get_points(self):
        # X will always increase starter -> ender
        if self.start[0] < self.end[0]:
            starter = self.start
            ender = self.end
        else:
            starter = self.end
            ender = self.start

        # Align other axis
        if starter[0] == ender[0]:
            if ender[1] > starter[1]:
                inc = (0, 1)
            else:
                inc = (0, -1)
        elif starter[1] == ender[1]:
            if ender[0] > starter[0]:
                inc = (1, 0)
            else:
                inc = (-1, 0)
        else:
            if ender[1] > starter[1]:
                inc = (1, 1)
            else:
                inc = (1, -1)

        points = []
        while starter != ender:
            points.append(starter.copy())
            starter[0] += inc[0]
            starter[1] += inc[1]
        points.append(ender.copy())
        return points


def get_line_segments(lines: List[str]) -> List[Line]:
    segments = []
    for l in lines:
        start, end = [[int(x) for x in point.split(',')]
                      for point in l.split("->")]
        segments.append(Line(start, end))
    return segments


def run_part_a(vents) -> int:
    segments = get_line_segments(vents)
    segments = [s for s in segments if s.is_straight()]

    intersects = Counter()
    for s in segments:
        for p in s.get_points():
            intersects[tuple(p)] += 1
        # intersects.update(s.get_points())

        # print(s)
        # print(s.get_points())

    return len([x for x in intersects.most_common(len(intersects)) if x[1] > 1])


def run_part_b(vents):
    segments = get_line_segments(vents)
    intersects = Counter()
    for s in segments:
        for p in s.get_points():
            intersects[tuple(p)] += 1

        print(s)
        print(s.get_points())

    return len([x for x in intersects.most_common(len(intersects)) if x[1] > 1])
    pass


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def test_part_a():
    expected = 5
    actual = run_part_a(read_input('test5.in'))

    assert actual == expected, f'Actual {actual} expected {expected}'


def test_part_b():
    expected = 12
    actual = run_part_b(read_input('test5.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


# test_part_a()
#print(f'Part A: {run_part_a(read_input("day5.in"))}')

test_part_b()
print(f'Part A: {run_part_b(read_input("day5.in"))}')

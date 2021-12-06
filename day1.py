

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines


def run_part_a(depth_readings):
    # depth_readings = [int(x) for x in depth_readings]
    # prev = depth_readings[0]
    # total_inc = 0
    total_inc = sum([int(b) > int(a) for (a, b) in zip(
        depth_readings, depth_readings[1:])])
    # for curr in depth_readings[1:]:
    #     if curr > prev:
    #         total_inc += 1
    #     prev = curr
    return total_inc


def run_part_b(depth_readings):
    depth_readings = [int(x) for x in depth_readings]
    prev_sum = None
    total_inc = 0
    running_sum = sum(depth_readings[:2])

    for i in range(2, len(depth_readings)):
        curr = depth_readings[i]
        running_sum += curr
        if prev_sum is not None:
            total_inc += (running_sum > prev_sum)
        prev_sum = running_sum
        running_sum -= depth_readings[i-2]
    return total_inc


def run_part_b_cg(dr):
    dr = [int(x) for x in dr]
    sums = [sum(x) for x in zip(dr, dr[1:], dr[2:])]
    return sum([b > a for (a, b) in zip(sums, sums[1:])])


_TEST_INPUT1 = [
    "199",
    "200",
    "208",
    "210",
    "200",
    "207",
    "240",
    "269",
    "260",
    "263",
]


def test_part_a():
    expected = 7
    actual = run_part_a(_TEST_INPUT1)
    if actual != expected:
        print(f'ERROR: {expected} != {actual}')


def test_part_b():
    expected = 5
    actual = run_part_b(_TEST_INPUT1)
    if actual != expected:
        print(f'ERROR: {expected} != {actual}')


# Part A answer: 1713
# test_part_a()
# print(run_part_a(read_input('day1.in')))

# Part B answer: 1734
# test_part_b()
# print(f'Part B (real): {run_part_b(read_input("day1.in"))}')

print(run_part_b_cg(_TEST_INPUT1))
print(f'Part B (real): {run_part_b_cg(read_input("day1.in"))}')

# From reddit

# solve = lambda data, diff: sum(b > a for a, b in zip(data, data[diff:]))
#
# print(solve(data, 1))
# print(solve(data, 3))

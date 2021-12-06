
from collections import Counter


def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines


def run_part_a(readings):
    num_bits = len(readings[0].rstrip())
    gamma_bits = []
    epsilon_bits = []

    for n in range(num_bits):
        vals = [r[n] for r in readings]
        c = Counter(vals)
        g, e = c.most_common()
        gamma_bits.append(g[0])
        epsilon_bits.append(e[0])

    return int("".join(gamma_bits), 2) * int("".join(epsilon_bits), 2)


def run_part_b(readings):

    nums = readings.copy()
    bit_n = 0
    while len(nums) > 1:
        vals = [r[bit_n] for r in nums]
        c = Counter(vals)
        g, e = c.most_common()
        if g[1] == e[1]:
            g = ('1', 1)
        nums = [x for x in nums if x[bit_n] == g[0]]
        bit_n += 1
        print(f'n:{bit_n} nums:{nums}')
    oc2 = nums[0]

    nums = readings.copy()
    bit_n = 0
    while len(nums) > 1:
        vals = [r[bit_n] for r in nums]
        c = Counter(vals)
        g, e = c.most_common()
        if g[1] == e[1]:
            e = ('0', 0)
        nums = [x for x in nums if x[bit_n] == e[0]]
        bit_n += 1
    co2 = nums[0]
    return int(co2, 2)*int(oc2, 2)


_TEST_INPUT1 = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]


def test_part_b():
    expected = 230
    actual = run_part_b(_TEST_INPUT1)

    assert actual == expected


def test_part_a():
    expected = 198
    actual = run_part_a(_TEST_INPUT1)

    assert actual == expected


# test_part_a()
#print(f'Part A: {run_part_a(read_input("day3.in"))}')

test_part_b()
print(f'Part B: {run_part_b(read_input("day3.in"))}')

"""
forward 8
down 6
down 8
forward 7
down 5
up 2
"""


from typing import List


def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines


_TEST_INPUT1 = [
    "forward 8",
    "down 6",
    "down 8",
    "forward 7",
    "down 5",
    "up 2"
]


def run_part_a(commands: List[str]):
    pos = [0, 0, 0]  # X,Y,Aim
    for c in commands:
        cmd, amt = c.split(" ")
        amt = int(amt)
        if cmd == "forward":
            pos[0] += amt
            pos[1] += pos[2] * amt
        elif cmd == "down":
            pos[2] += amt
        elif cmd == "up":
            pos[2] -= amt
        else:
            raise("Hell")

    return pos[0] * pos[1]


print(run_part_a(read_input('day2.in')))

from typing import List
import pprint
import logging
import sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)


def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)


WIN_POS_ = [
    0b1111100000000000000000000,
    0b0000011111000000000000000,
    0b0000000000111110000000000,
    0b0000000000000001111100000,
    0b0000000000000000000011111,
    0b1000010000100001000010000,
    0b0100001000010000100001000,
    0b0010000100001000010000100,
    0b0001000010000100001000010,
    0b0000100001000010000100001,
]


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        return lines


def idx_to_offset(x, y):
    return 5*x + y


def board_to_arr(board):
    ret = [-1]*(len(board)**2)
    for x in range(len(board)):
        for y in range(len(board)):
            ret[idx_to_offset(x, y)] = board[x][y]
    ret.reverse()
    return ret


def update_board_state(board_state, board: List, num):
    try:
        idx = board.index(num)
        logging.debug(
            f'Found {num} at {idx}')
        return setBit(board_state, idx)
    except:
        return None


def check_win(board_state):
    for combo in WIN_POS_:
        if combo & board_state == combo:
            return True


def calc_return(board: List, board_state, gotem):
    # This is stupid and can be made constant time with a mask
    #mask = 1
    unmarked_sum = 0
    for idx in range(len(board)):
        if not testBit(board_state, idx):
            unmarked_sum += board[idx]
    #    mask = mask << 1
    print(
        f'Calculating win for {board} {bin(board_state)} {gotem} got sum {unmarked_sum}')
    return gotem * unmarked_sum


def run_part_a(inputs: List[str]):
    draws = [int(x) for x in inputs[0].split(',')]
    boards_repr = []
    boards = []
    for line in inputs[1:]:
        if len(line) == 0:
            boards_repr.append([])
            continue
        boards_repr[-1].append([int(x) for x in line.split()])
    pprint.pprint(boards_repr)

    boards = [board_to_arr(b) for b in boards_repr]
    print(boards)
    board_states = [0]*(len(boards))

    boards_won = []
    for d in draws:
        logging.debug(f'\nDrawing {d}')

        for idx in range(len(boards)):
            logging.debug(
                f'Updating board {idx} currently at {bin(board_states[idx])}')

            b = boards[idx]
            update = update_board_state(board_states[idx], b, d)
            if update is not None:
                board_states[idx] = update
            logging.debug(f'Board state {bin(board_states[idx])}')

            if (idx not in boards_won) and check_win(board_states[idx]):
                boards_won.append(idx)
                if len(boards_won) == len(boards):
                    print("Got em")
                    return calc_return(b, board_states[idx], d)


def test_part_a():
    expected = 4512
    actual = run_part_a(read_input('test4.in'))

    assert actual == expected


def test_part_b():
    expected = 1924
    actual = run_part_a(read_input('test4.in'))

    assert actual == expected, f'{actual} and we wanted {expected}'


test_part_b()
print(f'Part B: {run_part_a(read_input("day4.in"))}')

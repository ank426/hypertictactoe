import os

import numpy as np


def check(board: np.ndarray) -> int | None:
    if 0 not in board:
        return 0

    n = board.ndim

    for i in range(n):
        sum = board.sum(axis=i, keepdims=True)
        if 3 in sum:
            return 1
        if -3 in sum:
            return -1

    if n < 2:
        return None

    for i in range(n):
        for j in range(i + 1, n):
            if ret := check(board.diagonal(axis1=i, axis2=j)):
                return ret
            if ret := check(np.flip(board, axis=i).diagonal(axis1=i, axis2=j)):
                return ret


n = int(input("Enter num of dimensions: "))
board = np.zeros((3,) * n, dtype=np.int8)

os.system("clear")
print(board)

t = True
while True:
    print(f"{'X' if t else 'O'}'s turn.")

    c = tuple(map(int, input("Coords: ").split()))
    if len(c) != n:
        print("Wrong num of dims. Try again.")
        continue
    for e in c:
        if not 0 <= e < n:
            print("Wrong input. Try again.")
            continue
    if board[*c] != 0:
        print("Already there. Try again.")
        continue

    board[*c] = 1 if t else -1

    os.system("clear")
    print(board)

    if (end := check(board)) is not None:
        if end == 1:
            print("X wins")
        elif end == -1:
            print("O wins")
        else:
            print("Draw")
        break

    t = not t

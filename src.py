from tinygrad import Tensor, dtypes

board = Tensor.zeros(3, 3, 3, dtype=dtypes.int8).contiguous()
print(board.numpy())

t = 1
while True:
    c = tuple(map(int, input("coords: ").split()))
    if c == (-1,):
        break
    board[*c] = t
    print(board.numpy())
    t *= -1


def check(board: Tensor) -> str | None:
    n = board.ndim

    for i in range(n):
        sum = board.sum(axis=i)
        if 3 in sum.numpy():
            print("X has won")
            return
        if -3 in sum.numpy():
            print("O has won")
            return

    if n < 2:
        return

    for i in range(n):
        for j in range(i + 1, n):
            check(Tensor(board.numpy().diagonal(axis1=i, axis2=j)))
            check(Tensor(board.flip(axis=i).numpy().diagonal(axis1=i, axis2=j)))


check(board)

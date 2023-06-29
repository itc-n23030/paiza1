import math


def f(n, m):
    return math.ceil(m / (n * 2))


n, m = [int(input()) for i in range(2)]
print(f(n, m))

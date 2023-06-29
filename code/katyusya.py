import math


def f(n, p, m, q):
    return (p * n) + q * (math.ceil(n / m))


n, p = list(map(int, input().split()))
m, q = list(map(int, input().split()))
print(f(n, p, m, q))

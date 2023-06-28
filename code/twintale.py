def f(c, p):
    return "1" if c[0] / c[1] > p[0] / p[1] else "2"


print(f(list(map(int, input().split())), list(map(int, input().split()))))

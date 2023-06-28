def f(s, n):
    return "OK" if s >= n else "NG"


s, n = list(map(int, input().split()))
print(f(s, n))

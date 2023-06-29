def f(n, m):
    return "ok" if m % n == 0 else "ng"


n, m = list(map(int, input().split()))
print(f(n, m))

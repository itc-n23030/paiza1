def f(n, s):
    return "_".join(s)


n = int(input())
s = [input() for i in range(n)]
print(f(n, s))

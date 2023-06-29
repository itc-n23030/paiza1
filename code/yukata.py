def f(N, s, t):
    n = 0
    m = 0
    for i in range(24):
        if tt[i] == "in":
            n += 5
        elif tt[i] == "out":
            n += 3
        if n > 0:
            n -= 1
            m += 2
        else:
            m += 1
    return m


tt = ["None"] * 24
N = int(input())
for i in range(N):
    s, t = input().split()
    tt[int(s)] = t
print(f(N, s, t))

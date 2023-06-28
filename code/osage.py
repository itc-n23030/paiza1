def f(n, m, t):
    a = n * 60
    s = 0
    for tt in t:
        if tt < a:
            a -= tt
            s += 1
        else:
            break
    return "OK" if s == m else s


n = int(input())
m = int(input())
t = [int(input()) for i in range(m)]
print(f(n, m, t))

def f(s, t):
    l = list("-" * s)
    l[t - 1] = "+"
    return "".join(l)


s, t = int(input()), int(input())
print(f(s, t))

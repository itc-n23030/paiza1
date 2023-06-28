a = 0


def f(d, e):
    return "OK" if a >= 3 else "NG"


for i in range(5):
    d, e = input().split()
    if d == e:
        a += 1
r = f(d, e)
print(r)

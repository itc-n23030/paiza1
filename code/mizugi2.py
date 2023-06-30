def f(x):
    a = 1
    c5 = 0
    for i in range(1, N + 1):
        n = i
        while n % 5 == 0:
            n //= 5
            c5 += 1

    for i in range(1, N + 1):
        n = i
        while n % 5 == 0:
            n //= 5

        while n % 2 == 0 and c5 > 0:
            n //= 2
            c5 -= 1

        a = (a * n) % 1000000000
    return a


N = int(input())
print(f(N))

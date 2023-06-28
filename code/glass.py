def f(N, a):
    a.sort()
    return a[N//2]


N = int(input())
a = list(map(int, input().split()))
print(f(N, a))

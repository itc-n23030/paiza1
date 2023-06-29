def f(M, N):
    return M - N if M - N > 0 else "0"


M, N = list(map(int, input().split()))
print(f(M, N))

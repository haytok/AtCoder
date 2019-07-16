N, M = map(int, input().split())

if M >= 2 * N:
    print((N + (M - N*2) // 4))
else:
    print(M//2)

# 数式に抽象化する
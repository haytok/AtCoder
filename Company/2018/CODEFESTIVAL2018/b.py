N, M, A, B = map(int, input().split())

bool = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    for i in range(a-1, b):
        if not bool[i]:
            bool[i] = not bool[i]

a = bool.count(True)

print(a*A+(N-a)*B)
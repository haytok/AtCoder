N, M = map(int, input().split())

inputs = [[i for i in input().split()] for _ in range(N)]

ans = set(inputs[0])
for item in inputs:
    ans &= set(item[1:])

print(len(ans))

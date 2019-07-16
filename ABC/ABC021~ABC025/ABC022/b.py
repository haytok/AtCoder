from collections import Counter

N = int(input())
inputs = [int(input()) for _ in range(N)]

kafun = Counter(inputs)
result = 0

for value in kafun.values():
    if value >= 2:
        result += value - 1

print(result)
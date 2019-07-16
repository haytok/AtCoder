from itertools import accumulate

N = int(input())

results = [0] * 1000002

for n in range(N):
    start, end = map(int, input().split())
    results[start] += 1
    results[end+1] -= 1

print(max(accumulate(results)))

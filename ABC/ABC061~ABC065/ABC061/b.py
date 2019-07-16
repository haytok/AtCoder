from collections import Counter

N, M = map(int, input().split())
input_counter = Counter()

for i in range(1, N+1):
        input_counter[int(i)] = 0

for j in range(M):
    for i in input().split():
        input_counter[int(i)] += 1

for element in input_counter.keys():
    print(input_counter[element])
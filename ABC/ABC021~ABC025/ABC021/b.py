from collections import Counter

N = int(input())
a, b = map(int, input().split())
K = int(input())
inputs = [int(i) for i in input().split()]
inputs_counter = Counter(inputs)

for value in inputs_counter.values():
    if value > 1:
        print('NO')
        break
else:
    if a in inputs:
        print('NO')
    elif b in inputs:
        print('NO')
    else:
        print('YES')
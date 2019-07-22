import math

N, D = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(N)]

def compute(point1, point2):
    length = 0
    for item1, item2 in zip(point1, point2):
        length += (item1 - item2) ** 2
    return 1 if int(math.sqrt(length)) ** 2 == length else 0

count = 0
for i in range(N):
    for j in range(i, N):
        if i != j:
            count += compute(inputs[i], inputs[j])

print(count)
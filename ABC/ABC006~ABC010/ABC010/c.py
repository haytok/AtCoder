import math

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())

distance = 10 ** 15

for _ in range(n):
    x, y = map(int, input().split())

    distance = min(distance,
    math.sqrt((txa - x) ** 2 + (tya - y) ** 2) + math.sqrt((txb - x) ** 2 + (tyb - y) ** 2)
    )

print('YES' if distance / V <= T else 'NO')

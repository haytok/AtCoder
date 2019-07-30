N = int(input())
inputs = [int(i) for i in input().split()]

count = 0
for a, b in zip((sorted(inputs)), inputs):
    if a != b:
        count += 1
print('YES' if count == 0 or count == 2 else 'NO')
N, M = map(int, input().split())

counts = 4 * N - M

for b in range(counts + 1):
    diff = counts - b
    if diff % 2 == 0 and N - diff // 2 - b >= 0:
        print(diff // 2, b, N - diff // 2 - b)
        break
else:
    print('-1 -1 -1')


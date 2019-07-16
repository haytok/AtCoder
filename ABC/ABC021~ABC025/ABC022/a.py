N, S, T = map(int, input().split())

W = 0
count = 0

for i in range(N):
    W += int(input())
    if S <= W <= T:
        count += 1

print(count)
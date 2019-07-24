N, K = map(int, input().split())
inputs = [int(i) for i in input().split()]

ans = 0
left = 0
total = 0

for i in range(N):
    total += inputs[i]
    while total >= K:
        total -= inputs[left]
        left += 1
    ans += left

print(ans)


"""
右側を固定すると、考えやすい。
"""
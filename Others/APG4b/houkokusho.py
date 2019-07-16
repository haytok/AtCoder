N = int(input())
inputs = [int(i) for i in input().split()]

data = [[] for _ in range(N)]
for i in range(1, N):
    data[inputs[i-1]].append(i)

print(data)
ans = 0
def compute(child, count, data):
    global ans
    if not data[child]:
        return count
    
    count += 1
    for item in data[child]:
        total = compute(item, count, data)
        # Noneが返るのは再帰が一番深いとこまで回っていない時
        if total is not None and total > ans:
            ans = total

compute(0, 0, data)

print(ans)

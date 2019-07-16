N, M = map(int, input().split())
inputs = [int(input()) for _ in range(M)][::-1] # 反対にあるもの順で先頭から並ぶ

ans = []
sets = set()
for item in inputs:
    if item not in sets:
        ans.append(item)
    sets.add(item)

for i in range(1, N+1):
    if i not in sets: # ここをans(配列)にするとTLEになる
        ans.append(i)

print(*ans, sep='\n')

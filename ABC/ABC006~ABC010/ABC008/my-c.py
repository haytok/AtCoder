N = int(input())
inputs = [int(input()) for _ in range(N)]

ans = 0

for i in inputs:
    # 次のfor文でi自身も回ってくるので初期化段階で-1しておく
    s = -1
    for j in inputs:
        if i % j == 0:
            s += 1
    ans += (s // 2 + 1) / (s + 1)

print(ans)

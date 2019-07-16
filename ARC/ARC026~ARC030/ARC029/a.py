N = int(input())
inputs = [int(input()) for _ in range(N)]

ans = []
# 桁数だけ回す。
for i in range(2 ** N):
    former, latter = 0, 0
    for j in range(N):
        # 右にシフトして、1が立っているかを判断する。
        if (i >> j) & 1 == 1:
            former += inputs[j]
        else:
            latter += inputs[j]
    ans.append(max(former, latter))

print(min(ans))

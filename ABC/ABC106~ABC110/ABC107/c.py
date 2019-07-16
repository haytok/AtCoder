# 無駄なところも数えて良いっていう考え方もある。
# 常に最適化しないといけないわけではない

N, K = map(int, input().split())
x = [int(i) for i in input().split()]

time = 10 ** 20

for i in range(N - K + 1):
    x_min = x[i]
    x_max = x[i + K - 1]
    if x_min >= 0:
        this_time = x_max
    elif x_max <= 0:
        this_time = abs(x_min)
    else:
        this_time = x_max - x_min + min(x_max, abs(x_min))

    if time > this_time:
        time = this_time

print(time)
N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ans = 10 ** 15

def cal(x):
    return max((E*N - H - (E + B) * x) // (E + D) + 1, 0)

for x in range(N):
    y = cal(x)
    ans = min(ans, A * x + C * y)

print(ans)

# import math

# N, H = map(int, input().split())
# A, B, C, D, E = map(int, input().split())

# ans = 10 ** 15

# """
# 0 <= x <= N,0 <= y <= N の束縛条件下で
# y >= {E*N - H - (E + B) * x} / (E + D)
# を満たすx, y を求める。
# """

# def cal(x):
#     return max(math.ceil((E*N - H - (E + B) * x) / (E + D)), 0)

# for x in range(N+1):
#     y = cal(x)
#     if H + B * x + D * y - E * (N - x - y) > 0:
#         ans = min(ans, A * x + C * y)

# print(ans)
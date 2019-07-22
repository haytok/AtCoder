import math

S = int(input())

ans = [0, 0]
if S <= 10 ** 9:
    ans += [S, 0, 0, 1]
else:
    root = math.ceil(math.sqrt(S))
    ans += [root ** 2 - S, root, root, 1]

print(*ans)

"""
探索せずとも一意に値が決まり切る問題
"""
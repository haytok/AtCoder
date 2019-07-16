from collections import deque

n = int(input())
ans = deque()
mod = 10007

for i in range(n):
    if i == 0:
        ans.append(0)
    elif i == 1:
        ans.append(0)
    elif i == 2:
        ans.append(1)
    else:
        ans.append((ans[i-1] + ans[i-2] + ans[i-3]) % mod )

print(ans[-1])

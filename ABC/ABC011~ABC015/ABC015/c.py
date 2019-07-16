N, K = map(int, input().split())
inputs = [[int(i) for i in input().split()] for _ in range(N)]

def dfs(n, ans):
    if n == N:
        return ans == 0
    for k in range(K):
        if dfs(n + 1, ans ^ inputs[n][k]):
            return True

print('Found' if dfs(0, 0) else 'Nothing')

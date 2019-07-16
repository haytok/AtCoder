N, K = map(int, input().split())

mod = [i for i in range(K, N+1, K)]
ans = len(mod) ** 3

if K % 2 == 0:
    items = [i for i in range(K//2, N+1, K)]
    ans += len(items) ** 3

print(ans)

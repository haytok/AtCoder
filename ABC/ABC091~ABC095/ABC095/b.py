N, X = map(int, input().split())
m = [ int(input()) for i in range(N) ]

rest = X - sum(m)
print(N + rest // min(m))
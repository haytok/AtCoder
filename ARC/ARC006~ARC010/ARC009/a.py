ans = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans += a * b

print(int(ans * 1.05))

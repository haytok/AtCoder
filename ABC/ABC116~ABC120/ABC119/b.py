N = int(input())

ans = 0
for _ in range(N):
    value, kahei = input().split()
    value = float(value)
    ans += value if kahei == 'JPY' else 380000 * value

print(ans)

R, G, B, N = map(int, input().split())

ans = 0
for r in range(N // R + 1):
    for g in range((N - R * r) // G + 1):
        tmp = N - r * R - g * G
        if tmp % B == 0:
            ans += 1

print(ans)

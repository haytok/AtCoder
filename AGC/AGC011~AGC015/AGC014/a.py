A, B, C = map(int, input().split())

ans = 0

if A == B == C and A % 2 == 0:
    ans = -1
else:
    while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
        A, B, C = (B + C) // 2, (C + A) // 2, (A + B) // 2
        ans += 1

print(ans)

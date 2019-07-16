A, B = map(abs, map(int, input().split()))

ans = 'Draw'
if A < B:
    ans = 'Ant'
elif A > B:
    ans = 'Bug'

print(ans)

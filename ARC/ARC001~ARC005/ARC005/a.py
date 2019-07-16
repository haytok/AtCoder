N = int(input())

ans = 0
for item in input().split():
    if item.replace('.', '') in ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun']:
        ans += 1

print(ans)

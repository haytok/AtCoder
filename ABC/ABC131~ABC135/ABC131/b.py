N, L = map(int, input().split())

tastes = [i for i in range(L, L+N)]
sum_tastes = sum(tastes)
if tastes[0] * tastes[-1] < 0:
    ans = sum_tastes
elif tastes[0] >= 0:
    ans = sum_tastes - tastes[0]
else:
    ans = sum_tastes - tastes[-1]

print(ans)

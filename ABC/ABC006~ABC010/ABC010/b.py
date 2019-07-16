n = int(input())

lists = [0, 0, 1, 0, 1, 2, 3, 0, 1, 0]
ans = 0

for i in input().split():
    ans += lists[int(i)]

print(ans)
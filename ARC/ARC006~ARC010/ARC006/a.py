treasure = [int(i) for i in input().split()]
B = int(input())
inputs = [int(i) for i in input().split()]

counts = 0
ans = 0
for item in inputs:
    if item in treasure:
        counts += 1

if counts == 6:
    ans = 1
elif counts == 5 and B in inputs:
    ans = 2
elif counts == 5:
    ans = 3
elif counts == 4:
    ans = 4
elif counts == 3:
    ans = 5

print(ans)

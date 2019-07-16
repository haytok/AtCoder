S = input()

first_splits = S.split('+')
second_splits = []
ans = 0

for i in first_splits:
    if '0' not in i.split('*'):
        ans += 1

print(ans)

# 別解１
# print(sum([int(not '0'in x) for x in input().split('+')]))
N = int(input())

ans = 0
dicts = {'tail': 0, 'head': 0, 'head_tail': 0}
for i in range(N):
    item = input()
    if 'AB' in item:
        ans += 1
    if item[0] == 'B' and item[-1] == 'A':
        dicts['head_tail'] += 1
    else:
        if item[-1] == 'A':
            dicts['tail'] += 1
        if item[0] == 'B':
            dicts['head'] += 1

# if dicts['tail'] == 0:
#     ans += min(dicts['head'], dicts['head_tail'])
# else:


a = min(dicts['tail'], dicts['head'])
ans += a
dicts['head'] -= a
dicts['tail'] -= a
# diff = max(dicts['tail'], dicts['head']) - min(dicts['tail'], dicts['head'])

if dicts['head_tail'] > 0:
    ans += dicts['head_tail'] - 1
    if dicts['head'] > 0:
        ans += 1
    if dicts['tail'] > 0:
        ans += 1
print(ans)

'''
-A
B-
B-A
'''

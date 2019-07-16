S = input()

dicts = {'O': '0', 'D': '0', 'I': '1', 'Z': '2', 'S': '5', 'B': '8'}
ans = ''
for item in S:
    if item in dicts:
        ans += dicts[item]
    else:
        ans += item

print(ans)

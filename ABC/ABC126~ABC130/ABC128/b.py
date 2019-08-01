N = int(input())

dicts = {}
for i in range(N):
    key, value = input().split()
    value = int(value)
    if key not in dicts:
        dicts[key] = [[value, i+1]]
    else:
        dicts[key].append([value, i+1])

dicts = sorted(dicts.items())
for values in dicts:
    for item in sorted(values[1], reverse=True):
        print(item[1])

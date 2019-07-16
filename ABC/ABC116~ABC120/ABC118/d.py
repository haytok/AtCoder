N, M = map(int, input().split())
inputs = [int(i) for i in input().split()]

if 6 in inputs and 9 in inputs:
    inputs.remove(6)

if 2 in inputs and 3 in inputs and 5 in inputs:
    inputs.remove(2)
    inputs.remove(3)
elif 2 in inputs and 3 in inputs:
    inputs.remove(2)
elif 2 in inputs and 5 in inputs:
    inputs.remove(2)
elif 3 in inputs and 5 in inputs:
    inputs.remove(3)

dicts = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

can_use = {}
for key in inputs:
    can_use[key] = dicts.get(key)

can_use = sorted(can_use.items(), key=lambda x: x[1])
can_use_counts = [item[1] for item in can_use]

print(can_use_counts)

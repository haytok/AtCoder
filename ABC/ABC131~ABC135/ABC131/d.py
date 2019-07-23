N = int(input())
inputs = [[int(i) for i in input().split()] for _ in range(N)]

inputs.sort(key=lambda x: x[1])
time = 0
for item in inputs:
    time += item[0]
    if time > item[1]:
        print('No')
        break
else:
    print('Yes')

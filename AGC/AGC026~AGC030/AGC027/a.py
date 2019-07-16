N, x = map(int, input().split())
inputs = [int(i) for i in input().split()]

inputs.sort()
ans = 0
limit = 0
for i in range(len(inputs)):
    if i == N - 1 and x - inputs[i] != limit:
        break
    elif x - limit >= inputs[i]:
        ans += 1
        limit += inputs[i]
    else:
        limit += inputs[i]

print(ans)

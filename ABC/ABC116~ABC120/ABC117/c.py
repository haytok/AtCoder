N, M = map(int, input().split())
inputs = [int(i) for i in input().split()]

inputs.sort()

diff = []
for i in range(M-1):
    diff.append(inputs[i+1] - inputs[i])

diff.sort(reverse=True)

print(inputs[-1] - inputs[0] - sum(diff[:N-1]))

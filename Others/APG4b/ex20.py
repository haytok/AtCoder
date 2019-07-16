N = int(input())
inputs = [int(i) for i in input().split()]

data = [[] for _ in range(N)]
for i in range(1, N):
    data[inputs[i-1]].append(i)

def compute(child, data):
    if not data[child]:
        return 1
    
    count = 0
    for item in data[child]:
        count += compute(item, data)
    count += 1
    return count

for i in range(N):
    print(compute(i, data))

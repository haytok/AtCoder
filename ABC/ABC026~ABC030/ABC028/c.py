inputs = list(map(int, input().split()))

total = sum(inputs)
cal = []

for i in range(len(inputs)):
    for j in range(i+1, len(inputs)):
        cal.append(total - inputs[i] - inputs[j])

cal.sort()

print(cal[-3])

# 別解
A, B, C, D, E = map(int,input().split())

print(max(E + D + A, E + C + B))
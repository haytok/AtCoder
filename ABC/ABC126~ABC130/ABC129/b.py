N = int(input())
inputs = [int(i) for i in input().split()]

total = sum(inputs)
print(min([abs(total - 2 * sum(inputs[i:])) for i in range(1, N)]))

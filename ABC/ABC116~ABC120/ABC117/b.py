N = int(input())
inputs = [int(i) for i in input().split()]

print('Yes' if max(inputs) < sum(inputs) - max(inputs) else 'No')

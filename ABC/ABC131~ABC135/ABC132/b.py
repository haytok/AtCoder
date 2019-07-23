n = int(input())
inputs = [int(i) for i in input().split()]

count = 0
for i in range(1, n-1):
    if (inputs[i-1] < inputs[i] < inputs[i+1]) or (inputs[i+1] < inputs[i] < inputs[i-1]):
        count += 1

print(count)

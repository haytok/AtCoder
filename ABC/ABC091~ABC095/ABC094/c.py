N = int(input())
inputs = [int(i) for i in input().split()]

sorted_inputs = inputs[:]
sorted_inputs.sort()
left = sorted_inputs[N//2-1]
right = sorted_inputs[N//2]

for item in inputs:
    if item <= left:
        print(right)
    else:
        print(left)

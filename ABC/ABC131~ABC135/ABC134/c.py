N = int(input())
inputs = [int(input()) for _ in range(N)]

sorted_inputs = sorted(inputs, reverse=True)
for i in range(N):
    if sorted_inputs[0] == inputs[i]:
        print(sorted_inputs[1])
    else:
        print(sorted_inputs[0])

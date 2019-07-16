N = int(input())
inputs = [int(i) for i in input().split()]

slime = 10000

if N == 2 and inputs[0] == inputs[1]:
    print(1)
    exit()
else:
    for i in range(N):
        if i == 0 or i == N-1:
            continue
        else:
            if inputs[i-1] == inputs[i] == inputs[i+1]:
                inputs[i] = slime
                slime -= 1
            elif i+2 <= N-1 and inputs[i] == inputs[i+1] == inputs[i+2]:
                continue
            elif inputs[i-1] == inputs[i] or inputs[i] == inputs[i+1]:
                inputs[i] = slime
                slime -= 1

print(10000-slime)

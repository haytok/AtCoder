N = int(input())
inputs = [int(i) for i in input().split()]

slime = 10000

for i in range(N):
    if i == 0:
        continue
    else:
        if inputs[i] == inputs[i-1]:
            inputs[i] = slime
            slime -= 1

print(10000-slime)

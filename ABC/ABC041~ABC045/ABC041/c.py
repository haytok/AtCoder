N = int(input())

inputs = {}
index = 1

for input in input().split():
    inputs[index] = int(input)
    index += 1

for key, value in sorted(inputs.items(), key=lambda x: x[1], reverse=True):
    print(key)
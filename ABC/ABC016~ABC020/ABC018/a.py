inputs = [int(input()) for _ in range(3)]
copy_inputs = inputs[:]
copy_inputs.sort(reverse=True)

for input in inputs:
    print(copy_inputs.index(input)+1)

# [print(copy_inputs.index(input)+1) for input in inputs]

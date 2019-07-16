N = int(input())
inputs = [input() for _ in range(N)]
compare_inputs = [inputs[0]]

for n in range(1, N):
    if inputs[n] in compare_inputs:
        print('No')
        break
    else:
        if not inputs[n][0] == inputs[n-1][-1]:
            print('No')
            break
    compare_inputs.append(inputs[n])
else:
    print('Yes')

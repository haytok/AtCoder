from collections import Counter

N = int(input())
inputs = [int(i) for i in input().split()]

inputs.sort(reverse=True)
counter_inputs = Counter(inputs)
powers_of_two = [2**i for i in range(1, 31)]
ans = 0

for item in inputs:
    if counter_inputs[item] > 0:
        counter_inputs[item] -= 1
    
        while powers_of_two[-1] > 2 * item:
            powers_of_two.pop(-1)
        
        pair = powers_of_two[-1] - item
        if counter_inputs[pair] > 0:
            ans += 1
            counter_inputs[pair] -= 1
    
print(ans)

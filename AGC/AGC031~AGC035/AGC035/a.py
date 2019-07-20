N = int(input())
inputs = [int(i) for i in input().split()]

set_inputs = set(inputs)
if N % 3 == 0:
    list_inputs = list(set_inputs)
    if (len(set_inputs) == 3 
    and list_inputs[0] == (list_inputs[1] ^ list_inputs[2]) 
    and (inputs.count(list_inputs[0]) == inputs.count(list_inputs[1]) == inputs.count(list_inputs[2]))):
        print('Yes')
    elif len(set_inputs) == 2:
        list_inputs = list(set_inputs)
        if inputs.count(list_inputs[0]) > inputs.count(list_inputs[1]):
            more = list_inputs[0]
            less = list_inputs[1]
        else:
            more = list_inputs[1]
            less = list_inputs[0]
        print('Yes' if less == 0 and inputs.count(more) == inputs.count(less) * 2 else 'No')
    elif len(set_inputs) == 1:
        print('Yes' if inputs[0] == 0 else 'No')
    else:
        print('No')
else:
    print('Yes' if set_inputs == set([0]) else 'No')
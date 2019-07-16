from collections import Counter

inputs = list(input())

count = 10 ** 15
kinds = len(set(inputs))

def cal(inputs, item):
    re = ''
    for index in range(len(inputs)-1):
        if inputs[index] == item or inputs[index+1] == item:
            re += item
        else:
            re += inputs[index]
    return re

if kinds == 1:
    count = 0
else:
    set_inputs = set(inputs)
    for set_input in set_inputs:
        item = inputs[:]
        total = 0
        while len(set(item)) != 1:
            item = list(cal(item, set_input))
            total += 1
        count = min(count, total)

print(count)

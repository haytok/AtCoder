from collections import Counter

N = int(input())
input_list = sorted([int(i) for i in input().split()])
inupt_dict = (Counter(input_list))
result = 0
input_dict_keys = inupt_dict.keys()

if N == 1:
    result = 1
elif N == 2 and input_list[0] == input_list[1]:
    result = 2
elif N == 2 and input_list[0] != input_list[1]:
    if input_list[1] == input_list[0] + 1:
        result = 2
    else:
        result = 1
else:
    for i in range(N-2):
        if i in input_dict_keys:
            if i+1 in input_dict_keys:
                if i+2 in input_dict_keys:
                    result = max(result, (inupt_dict[i] + inupt_dict[i+1] + inupt_dict[i+2]))
    for i in range(N-1):
        if i in input_dict_keys:
            if i+1 in input_dict_keys:
                result = max(result, (inupt_dict[i] + inupt_dict[i+1]))
    for i in range(N):
        if i in input_dict_keys:
            result = max(result, inupt_dict[i])

print(result)
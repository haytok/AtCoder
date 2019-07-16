from collections import Counter

N = int(input())
input_list = sorted([int(i) for i in input().split()])
inupt_dict = Counter(input_list)
sorted_input_dict = sorted(dict(filter(lambda x:x[1]>1, inupt_dict.items())).items(), key=lambda x: x[0], reverse=True)
result = 1

if sorted_input_dict == []:
    result = 0
else:
    result *= sorted_input_dict[0][0]
    if sorted_input_dict[0][1] > 3:
        result *= sorted_input_dict[0][0]
    else:
        result *= sorted_input_dict[1][0]

print(result)

# from collections import Counter
# N = int(input())
# A = map(int, input().split())
# A=Counter(A)
# t = []
# for k, v in A.items():
#     if v > 1:
#         t.append(k)
#         if v > 3:
#             t.append(k)
# A = sorted(t,reverse=True)
# if len(A) < 2:
#     print(0)
# else:
#     print(A[0] * A[1])
s = input()
K = int(input())

list = []

for i in range(len(s)):
    if s[i] not in list:
        list.append(s[i])
    for j in range(2,len(s)+1):
        if (s[i:j] not in list) and s[i:j] !='' and len(s[i:j]) <= 5 :
            list.append(s[i:j])

list = sorted(list)
print(list[K-1])

# for i in range(len(s)):
#     if s[i] not in dict.keys():
#         dict[s[i]] = []
#         dict[s[i]].append(s[i])
#     for j in range(2,len(s)+1):
#         if (s[i:j] not in dict[s[i]]) and s[i:j] !='':
#             dict[s[i]].append(s[i:j])
#     dict[s[i]].sort()

# for key in dict.keys():
#     numberDict[key] = len(dict[key])

# for key in dict.keys():
#     num = K - len(dict[key])
#     result = key
#     if num < 0:
#         pass
# print(dict)



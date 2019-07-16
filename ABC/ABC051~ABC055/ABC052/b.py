N = int(input())
S = input()

# ruiseki = [0]

# for i in range(len(S)):
#     if S[i] == "I":
#         ruiseki.append(ruiseki[i] + 1)
#     elif S[i] == 'D':
#         ruiseki.append(ruiseki[i] - 1)

# print(max(ruiseki))

ans = 0
value = 0
for i in S:
    if i == "I":
        value += 1
    else:
        value -= 1
    ans = max(ans, value)

print(ans)
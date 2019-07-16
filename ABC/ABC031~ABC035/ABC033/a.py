N = input()

print('SAME' if N[0] == N[1] == N[2] == N[3] else 'DIFFERENT')

# 別解１
# print(["SAME","DIFFERENT"][len(set(input()))>1])

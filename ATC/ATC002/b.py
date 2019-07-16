N, mod, P = map(int, input().split())

print(pow(N % mod, P, mod))

# div = []

# for p in range(1, P+1):
#     item = (N ** p) % mod
#     if item not in div:
#         div.append(item)

# print(div)
# print('========')

# # for p in range(1, P):
# #     print(N**p%mod)
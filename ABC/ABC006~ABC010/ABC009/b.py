# N = int(input())

# ans = []

# for i in range(N):
#     item = int(input())
#     if item not in ans:
#         ans.append(item)

# ans.sort()

# print(ans[-2])

N = int(input())

inputs = sorted(list(set([int(input()) for _ in range(N)])))

print(inputs[-2])

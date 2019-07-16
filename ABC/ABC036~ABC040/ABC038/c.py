# N = int(input())
# inputs = [int(i) for i in input().split()]

# ans = N
# right = 1

# for left in range(N):
#     while right < N-1 and (left <= right or inputs[left] < inputs[right]):
#         right += 1
#     ans += (right - left)
#     if left == right :
#         right += 1

# print(ans)

# # 部分点解答
# N = int(input())
# inputs = [int(i) for i in input().split()]

# ans = N

# for i in range(N):
#     index = i
#     for j in range(i+1, N):
#         if inputs[index] < inputs[j]:
#             ans += 1
#             index += 1
#         else:
#             break

# print(ans)

# # 満点解答
# N = int(input())
# a = list(map(int, input().split()))

# ans = 0
# l = 1
# for i in range(1,N):
#     if a[i-1] < a[i]:
#         l += 1
#     else:
#         l = 1
#     ans += l

# print(int(ans)+1)
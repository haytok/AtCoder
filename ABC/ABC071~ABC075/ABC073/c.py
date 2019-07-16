from collections import Counter

N = int(input())
inupt_dict = Counter(int(input()) for i in range(N))
count = 0

for value in inupt_dict.values():
    count += (value%2)

print(count)

# print(sum([i % 2 for i in Counter([input() for _ in range(int(input()))]).values()]))

# n = int(input())
# s = set()
# for i in range(0,n):
#     a = input()
#     if a in s:
#         s.remove(a)
#     else:
#         s.add(a)
# print(len(s))

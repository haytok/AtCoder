from collections import Counter

N, A = map(int, input().split())
input_list = [int(i) - A for i in input().split()]

ans = Counter([0, input_list[0]])

for i in input_list[1:]:
    temp = Counter()
    for key, value in ans.items():
        temp[i + key] += value
    ans += temp

print(ans[0] - 1)

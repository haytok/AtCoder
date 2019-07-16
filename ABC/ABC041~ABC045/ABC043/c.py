N = int(input())
input_list = [int(i) for i in input().split()]

ans = 10 ** 20

for i in range(min(input_list), max(input_list)+1):
    ans1 = 0
    for input in input_list:
        ans1 += (i - input) ** 2
    ans = min(ans, ans1)

print(ans)

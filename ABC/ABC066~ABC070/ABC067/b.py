N, K = map(int, input().split())
input_list = sorted([int(i) for i in input().split()], reverse=True)

result = 0

for i in range(K):
    result += input_list[i]

print(sum(input_list[:K]))

# for分のところをsum(list[:K])と書いておけば、短く書ける
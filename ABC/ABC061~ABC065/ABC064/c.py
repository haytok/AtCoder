from collections import Counter

N = int(input())

count_counter = Counter()
result = 0
over = 0

for i in input().split():
    count_counter[int(i) // 400] += 1

for key in count_counter.keys():
    if key < 8:
        result += 1
    else:
        over += count_counter[key]

if result == 0:
    print(1, over)
else:
    print(result, result+over)
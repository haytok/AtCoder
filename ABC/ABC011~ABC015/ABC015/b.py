import math

N = int(input())

sum = 0
count = 0

for i in input().split():
    cast_item = int(i)
    if cast_item > 0:
        sum += cast_item
        count += 1

print(int(math.ceil(sum/count)))

from collections import Counter as C

N = int(input())
S = list(int(i) for i in input().split())
count = 0

for key, value in C(S).items():
    if key < value:
        count += (value-key)
    elif key > value:
        count += value

print(count)
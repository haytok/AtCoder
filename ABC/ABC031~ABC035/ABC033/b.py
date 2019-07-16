N = int(input())
inputs = [input().split() for i in range(N)]

total = 0
flag = 0

for input in inputs:
    total += int(input[1])

flag = total // 2 + 1

for input in inputs:
    if flag <= int(input[1]):
        print(input[0])
        break
else:
    print('atcoder')
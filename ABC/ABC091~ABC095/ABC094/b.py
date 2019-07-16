N, M, X = map(int, input().split())

count = 0
for i in input().split():
    if int(i) > X:
        break
    count += 1

print(min(count , M-count))
    
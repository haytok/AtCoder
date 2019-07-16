N, A, B = map(int, input().split())
count = 0

def cal(n):
    item = str(n)
    count = 0
    for i in range(len(item)):
        count += int(item[i])
    return count

for i in range(1, N+1):
    sum = cal(i)
    if A <= sum <= B:
        count += i

print(count)
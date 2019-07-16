N = int(input())
A = [int(i) for i in input().split()]
count = 10**9

def cal(num):
    sum = 0
    while True:
        if num % 2 == 0:
            sum += 1
            num /= 2
        else:
            break
    return sum

for i in range(N):
    count = min(cal(A[i]), count)
print(count)
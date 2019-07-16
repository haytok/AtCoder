N = int(input())
count = 0
result = 0

if N == 1:
    print(1)
else:
    for i in range(1, N+1):
        now_count = bin(i)[::-1].index("1")
        if now_count > count:
            count = now_count
            result = i
    print(result)

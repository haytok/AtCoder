N = int(input())
inputs = [int(input()) for _ in range(N)]

ans = 10 ** 7
for i in range(2 ** N):
    bit = format(i, 'b').zfill(N)
    time = [0, 0]
    for index in range(len(bit)):
        time[int(bit[index])] += inputs[index]
    ans = min(ans, max(time))

print(ans)

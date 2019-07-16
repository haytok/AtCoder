N = int(input())
T, A = map(int, input().split())

diff = 10 ** 15
index = 1
ans = 10 ** 15

def cal(H):
    return T - H * 0.006


for i in input().split():
    if abs(cal(int(i))-A) <= diff:
        diff = abs(cal(int(i))-A)
        ans = index
    index += 1

print(ans)

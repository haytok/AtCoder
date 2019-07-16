A, B, C ,D = map(int, input().split())

def cal(n):
    global B, D
    if B <= D:
        print(B-n)
    else:
        print(D-n)

if A >= D or B <= C:
    print(0)
elif A >= C:
    cal(A)
else:
    cal(C)

# a, b, c, d = map(int, input().split())
# print(max(0, min(b, d) - max(a, c) ))

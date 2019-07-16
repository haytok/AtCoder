A, B, C, K = map(int, input().split())

# def judge(n):
#     if abs(n) > 10**18:
#         print('Unfair')
#     else:
#         print(n)

# if K == 0:
#     judge(A-B)
# else:
#     if A == B and B == C and C == A :
#         print(0)
#     else:
        # sum = A + B + C
        # この文やとK(0<=K<=10**18)次第で爆発的なループになってしまうから別の方法を取る
        # for i in range(1, K+1):
        #     sum *= K
        #     A = sum - A
        #     B = sum - B
        # if K % 2 == 0:
        #     judge(A-B)
        # else:
        #     judge(B-A)

def judge(n):
    if abs(n) > 10**18:
        print('Unfair')
    else:
        print(n)

if K % 2 == 0:
    judge(A-B)
else:
     judge(B-A)
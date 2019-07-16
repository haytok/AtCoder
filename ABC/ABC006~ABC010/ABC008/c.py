n=int(input())
c=[int(input()) for _ in range(n)]
ans=0
for x in c:
    s=-1
    for y in c:
        if x%y==0:
            s+=1
    print(s)
    ans+=1/2 if s%2!=0 else (s+2)/(2*s+2)
print(ans)

# from itertools import permutations
# from math import factorial

# N = int(input())
# inputs = [int(input()) for _ in range(N)]
# # 最初は全て表
# counts = [1] * N
# # 表の期待値を求める
# total = factorial(N)


# for item in permutations(inputs, N):
#     for index in range(N-1):
#         mod = item[index]
#         for i in range(index)

# # あるコインに書かれた数字をCとした時に、どういう条件下で
# # そのコインが表を向いているかを考える

# # そのコインよりも左側にあるCの約数の数字が書かれたコインの個数が
# # 奇数なら裏、偶数なら表になる

# # 目標のコイン以外でCの約数となっているコインの数をS枚とする
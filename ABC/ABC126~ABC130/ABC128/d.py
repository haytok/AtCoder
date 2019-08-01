from collections import deque

N, K = map(int, input().split())
inputs = [int(i) for i in input().split()]

# NよりもKの方が大きいケースもあるのをケアしないといけない
# 結局先に配列から宝石を取り出す作業をするので、
# # 配列の長さの分(N)を全部取るか、最大限(K)取るかをのいずれか。
R = min(N, K) 
ans = 0
for left in range(R+1):
    for right in range(R+1-left):
        if left + right > K:
            continue
        stay = K - left - right
        tmp = inputs[:left] + inputs[::-1][:right]
        tmp.sort()
        total = sum(tmp)
        if stay <= len(tmp):
            tmp = tmp[:stay]
        for item in tmp:
            if item < 0:
                total -= item
            else:
                break
        ans = max(ans, total)

print(ans)

"""
tmp = inputs[:left] + inputs[::-1][:right]
配列の後ろから何番目まで取りたい時とかは逆順の前から何番目とか取るとわかりやすい。
"""

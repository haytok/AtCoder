W, a, b = map(int, input().split())

print(max(max(a, b)-min(a, b)-W, 0))

# 文法問題
# max(a, b)-min(a, b) <=> abs(a-b)
# 大きい方と小さい方の差は二つの絶対値に等しい
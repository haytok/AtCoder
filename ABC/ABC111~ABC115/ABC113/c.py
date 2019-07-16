N, M = map(int, input().split())

sorted_inputs = {}
ans = [None]*M

for i in range(M):
    P, Y = map(int, input().split())
    if sorted_inputs.get(P) is None:
        sorted_inputs[P] = [(Y, i)]
    else:
        sorted_inputs[P].append((Y, i))

for pref, l in sorted_inputs.items():
    l.sort() # Yでソートされる
    for j, (Y, i) in enumerate(l):
        first = str(pref).rjust(6, '0')
        latter = str(j+1).rjust(6, '0')
        ans[i] = first + latter

for item in ans:
    print(item)

# 無駄な計算をしていた箇所
# この２つをまとめれたら良かった。
# for input in sorted_inputs:
#     sorted_inputs[input].sort()

# for input in inputs:
#     first = str(input[0]).rjust(6, '0')
#     latter = str(sorted_inputs[input[0]].index(input[1])+1).rjust(6, '0')
#     print(first + latter)

N = int(input())

pointer = [[]]*(N+1)
salary = [0]*(N+1)

# 入力された数字(=上司の社員番号)から社員番号へのポインタをリストを用いて作成
for i in range(N-1):
    pointer[int(input())].append(i+2)

'''
例
[[], [2], [3, 6], [4, 5], [], [], []]
root  1       2       3   4   5   6
'''

for i in range(len(pointer)-1, 0, -1):
    # 末端すなはち一番の部下は給料が１
    if len(pointer[i]) == 0:
        salary[i] = 1
    # 末端でないとき
    else:
        temp = [salary[j] for j in pointer[i]]
        salary[i] = max(temp) + min(temp) + 1

print(salary[1])

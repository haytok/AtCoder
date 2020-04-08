# 計算量が多くて全テストケースを通せなかった解法
def main(N, A):
    ans = [0] * N
    max_value = 0
    for index in range(len(A)):
        target = A[index]
        if target <= N:
            ans[target - 1] += 1
        elif target > N:
            max_value = max(set(ans))
            ans = [max_value] * N
    return ans

# 模範解答
def solution(N, A):
    ans = [0] * N
    current_max = 0
    max_to_set = 0
    for index in range(len(A)):
        target = A[index]
        if target <= N:
            # target > N の時の処理の直後の処理
            if ans[target - 1] < max_to_set:
                ans[target - 1] = max_to_set
            # 一般的なケース
            ans[target - 1] += 1
            if ans[target - 1] > current_max:
                current_max = ans[target - 1]
        elif target > N:
            max_to_set = current_max
    return [max(max_to_set, value) for value in ans]

if __name__ == '__main__':
    A, N = [3, 4, 4, 6, 1, 4, 4], 5
    # A, N = [4, 4, 4, 4, 4], 3
    # A, N = [2], 2
    print(solution(N, A))

"""
- 計算量を落とすために、かなり難しかった
              c m
0 0 0 0 0  0: 0 0
0 0 1 0 0  0: 1 0
0 0 1 1 0  0: 1 0
0 0 1 2 0  0: 2 0
0 0 1 2 0  0: 2 2
3 0 1 2 0  0: 3 2
3 0 1 3 0  0: 3 2
3 0 1 4 0  0: 4 2

今の最大値と過去の最大がある
変化する点が二回ある
- インクリメントをする時
- 配列の値を全てその時の最大値にする時

current_max, max_to_set
"""
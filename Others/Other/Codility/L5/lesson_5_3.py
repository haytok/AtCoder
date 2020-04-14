def get_ruisekiwa(array):
    ans = [0]
    for index, value in enumerate(array):
        ans.append(ans[index] + value)
    return ans

def solution(A):
    ans = 1e10
    ans_index = -1
    ruisekiwa = get_ruisekiwa(A)
    length = len(A)
    for p in range(length):
        for q in range(p + 1, length):
            average = (ruisekiwa[q+1] - ruisekiwa[p]) / (q - p + 1)
            if ans > average:
                ans = average
                ans_index = p
    return ans_index


if __name__ == '__main__':
    array = [4, 2, 2, 5, 1, 5, 8]
    print(get_ruisekiwa(array))
    print(solution(array))

"""
やったことあるか or ないかは非常に重要
"""
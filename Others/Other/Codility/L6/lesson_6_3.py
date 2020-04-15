from itertools import combinations

def is_checked(A, former, latter):
    distance = abs(former - latter)
    return distance <= A[former] + A[latter]

def solution(A):
    indexes = [i for i in range(len(A))]
    ans = 0
    for item in combinations(indexes, 2):
        ans += 1 if is_checked(A, item[0], item[1]) else 0
    return ans if ans <= 1e7 else -1


if __name__ == '__main__':
    A = [1, 5, 2, 1, 4, 0]
    print(solution(A))
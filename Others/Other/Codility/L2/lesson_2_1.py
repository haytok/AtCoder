from collections import deque

def solution(A, K):
    deque_A = deque(A)
    deque_A.rotate(K)
    ans = list(deque_A)
    return ans

def main(A, K):
    length = len(A)
    if length == 0:
        ans = A
    else:
      moving_length  = K % length
      ans = A if moving_length == 0 else A[length - moving_length:] + A[:length - moving_length]
    return ans

if __name__ == '__main__':
    A, K = [i for i in range(10)], 2
    solution(A, K)
    main(A, K)
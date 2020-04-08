from collections import Counter

def solution(A):
    counter_A = Counter(A)
    for key, value in counter_A.items():
        if value % 2 == 1:
            return key
S = input()
N = int(input())

index = 1

for first in range(5):
    for second in range(5):
        if index == N:
            print(S[first] + S[second])
            exit()
        index += 1
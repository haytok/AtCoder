N, D = map(int, input().split())
X = [int(i) for i in input().split()]
X.insert(0, 0)
count = 0

for i in range(N):
    for j in range(i+1, N):
        if X[j] - X[i] > D:
            break
        else:
            for k in range(j+1, N):
                if X[k] - X[i] <= 2 * D:
                    if X[k] - X[j] <= D and X[k] - X[i] > D:
                        count += 1

print(count)

# def cal(first, second, third, D):
#     if second - first <= D and third - second <= D and third - first > D:
#         return 1
#     else:
#         return 0
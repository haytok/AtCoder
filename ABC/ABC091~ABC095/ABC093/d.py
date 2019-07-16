Q = int(input())
data = [[int(i) for i in input().split()] for i in range(Q)]
list = []

for i in range(Q):
    maxNumber = data[i][0] * data[i][1] - 1
    minData = min(data)
    list.append(maxNumber / firstNumber)
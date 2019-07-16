C = [[int(i) for i in input().split()] for i in range(3)]
minList = []

for i in range(3):
    if i == 0:
        minList = C[i]
    else:
        for j in range(3):
            minList[j] = min(minList[j], C[i][j])

for i in range(3):
    diff = [x-y for (x,y) in zip(C[i], minList)]
    if diff[0] == diff[1] == diff[2]:
        if i == 2:
            print("Yes")
    else:
        print("No")
        break
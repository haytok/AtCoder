N = int(input())
list = [[int(i) for i in input().split()] for i in range(N)]
list.insert(0, [0, 0, 0])

if N == 1:
    timeInterval = list[1][0] - list[0][0]
    distance = abs(list[1][1]+list[1][2]-list[0][1]-list[0][2])
    if timeInterval < distance:
        print("No")
    elif (timeInterval - distance)%2 == 0:
        print("Yes")
    else:
        print("No")
else:
    for i in range(N):
        timeInterval = list[i+1][0] - list[i][0]
        distance = abs(list[i+1][1]+list[i+1][2]-list[i][1]-list[i][2])
        if timeInterval < distance:
            print("No")
            break
        elif (timeInterval - distance)%2 == 0:
            if i == N-1:
                print("Yes")
        else:
            print("No")
            break
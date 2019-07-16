W, H, N = map(int, input().split())
input_list = [[int(i) for i in input().split()] for j in range(N)]

x_max, x_min, y_max, y_min = W, 0, H, 0

for i in range(N):
    if input_list[i][2] == 1:
        x_min = max(x_min, input_list[i][0])
    elif input_list[i][2] == 2:
        x_max = min(x_max, input_list[i][0])
    elif input_list[i][2] == 3:
        y_min = max(y_min, input_list[i][1])
    elif input_list[i][2] == 4:
        y_max = min(y_max, input_list[i][1])

if x_max - x_min > 0 and y_max - y_min > 0:
    print((x_max-x_min)*(y_max-y_min))
else:
    print(0)

N = int(input())
red = [[int(i) for i in input().split()] for i in range(N)]
red.sort(key=lambda x:x[1], reverse=True)
blue = sorted([[int(i) for i in input().split()] for i in range(N)])
count= 0

# 青の配列を回してる
for x_b, y_b in blue:
    for x_r, y_r in red:
        if x_b > x_r and y_b > y_r:
            red.remove([x_r, y_r])
            count += 1
            break
print(count)

            
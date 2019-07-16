A = int(input()) # 500円
B = int(input()) # 100円
C = int(input()) # 50円
X = int(input()) # 合計

price = [500, 100, 50]
count = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if price[0]*i + price[1]*j + price[2]*k == X:
                count+= 1
print(count)
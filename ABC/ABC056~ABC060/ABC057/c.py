import math
import time

t1 = time.time()
N = int(input())

ans = 100

# 桁数を数学的に計算する関数
def cal_digits(n):
    digits = 0
    while True:
        if n // 10 < 1:
            digits += 1
            break
        n //= 10
        digits += 1
    return digits

# 桁数を文字列にキャストしてから計算する関数
def cal_string(n1, n2):
    return max(len(str(n1)), len(str(n2)))

for i in range(1, int(math.sqrt(N))+1):
    if N % i == 0:
        ans = min(ans, max(cal_digits(i), cal_digits(N//i)))
        #ans = min(ans, cal_string(i, N//i))

print(ans)
print("passedTime:{}".format(time.time()-t1))

# 自分のｙやり方は愚直なやり方
# 桁が多きいほど数学的に計算する方が速く計算できる
# 桁が小さいときは、stringにキャストする方が速く計算できる

# 一方でエレガントな解法は、int(math.sqrt(N))+1にできるだけ近くて、
# その数の対になる数が答えになる

# N = int(input())

# x = int(pow(N, 0.5))
# while N % x != 0:
#     x -= 1
# print(len(str(N // x)))

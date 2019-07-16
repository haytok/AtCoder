from functools import lru_cache
# import time

# メモ化をしている
# 0,1,1,2,3...
# 時間を計測した結果、圧倒的に計算時間はメモ化した方が高速
@lru_cache(maxsize=None)
def fibo(n):
    start1 = time.time()
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


# def fibo1(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo1(n - 1) + fibo1(n - 2)

# a = 40
# start1 = time.time()
# print(fibo(a))
# elapsed_time = time.time() - start1
# print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")


# start2 = time.time()
# fibo1(a)
# elapsed_time = time.time() - start2
# print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

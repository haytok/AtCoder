from functools import reduce

N = int(input())
input_list = sorted([int(input()) for i in range(N)])

# ユークリッドの互除法
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

print(lcm(*input_list))
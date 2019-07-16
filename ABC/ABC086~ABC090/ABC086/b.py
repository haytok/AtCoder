import math

a, b = input().split()
union = int(a+b)
sqrtNumber = math.sqrt(union)

print('Yes'if int(sqrtNumber) ** 2 == union else 'No')
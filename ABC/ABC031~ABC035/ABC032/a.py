a = int(input())
b = int(input())
n = int(input())

def gcd(a, b):
    while b:
	    a, b = b, a % b
    return a

lcm = a * b // gcd(a, b)

if lcm >= n:
    print(lcm)
elif n % lcm == 0:
    print(n)
else:
    print(((n // lcm) + 1) * lcm)

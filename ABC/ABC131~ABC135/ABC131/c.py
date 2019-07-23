A, B, C, D = map(int, input().split())

def gcd(a, b):
    while b:
	    a, b = b, a % b
    return a

lcm = C * D // gcd(C, D)
total = B - A + 1
ans = total - ((B // C - (A - 1) // C) + (B // D - (A - 1) // D) - (B // lcm - (A - 1) // lcm))
print(ans)

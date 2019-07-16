N = int(input())
X = 0
n = N

while N != 0:
    X += (N % 10) 
    N //= 10
    
print("Yes" if n % X == 0 else "No")
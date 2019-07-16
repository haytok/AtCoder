N, mod, P = map(int, input().split())

tmp = 22
ans = 1

for i in range(10000):
    # i番目のフラグが立っているかを確認
    if bin(1 & (N**P)>>i) == bin(1):
        print(2 ** i)
        ans = ans * (2 ** i) % mod

print(ans)

for i in range(10): 
    # i番目のフラグが立っている時 
    if bin(1 & 25>>i) == bin(1): 
        print(2**i) 

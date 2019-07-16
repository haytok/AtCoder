A, B = map(int, input().split())

xor = [0, 1, 3]

def cal(n, flag=False):
    if n == 0:
        return 0
    else:
        if flag:
            n -= 1
        if n < 3:
            return xor[n]
        else:
            amari = (n - 3) % 4
            if amari == 0:
                return 0
            elif amari == 1:
                return n
            elif amari == 2:
                return 1
            elif amari == 3:
                return n ^ 1
        
print(cal(A, flag=True) ^ cal(B))

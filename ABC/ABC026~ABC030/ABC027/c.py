n = int(input())

x = 1
p = 1

if n == 1:
    print('Aoki')
else:
    while True:
        a = 2**(p*2)
        x += a
        if x >= n:
            print('Takahashi')
            break
        x += a
        if x >= n :
            print('Aoki')
            break
        p += 1

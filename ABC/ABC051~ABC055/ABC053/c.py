x = int(input())

if x <= 6:
    print(1)
elif 7 <= x <= 10:
    print(2)
else:
    div = x % 11
    shou = x // 11
    if div == 0:
        print(2 * shou)
    elif div <= 6:
        print(2 * shou + 1)
    else:
        print(2 * shou + 2)
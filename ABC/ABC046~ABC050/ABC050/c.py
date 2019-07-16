N = int(input())
input_list = sorted([int(i) for i in input().split()])

mod = 10 ** 9 + 7

if N % 2 == 1:
    if input_list[0] != 0:
        print(0)
    else:
        if N == 1:
            print(1)
        flag = 2
        limit = (N - 1) // 2
        for i in range(1, limit, 2):
            if input_list[i] == flag and input_list[i+1] == flag:
                flag += 2
                if i == limit-1:
                    print((2**limit) % mod)
            else:
                print(0)
                break
elif N % 2 == 0:
    flag = 1
    limit = N
    for i in range(0, limit, 2):
        if input_list[i] == flag and input_list[i+1] == flag:
            flag += 2
            if i == limit-2:
                print((2**(N//2)) % mod)
                break
        else:
            print(0)
            break


# 5
# 4 2 0 2 4
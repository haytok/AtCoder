N = int(input())
input_list = sorted([int(input()) for i in range(N)])

result = sum(input_list)

# 入力の総和が10の倍数でないときは、それが成績となる
if result % 10 != 0:
    print(result)
# 入力の総和が10の倍数のとき
else:
    for i in input_list:
        if i % 10 != 0:
            print(result-i)
            break
    else:
        print(0)

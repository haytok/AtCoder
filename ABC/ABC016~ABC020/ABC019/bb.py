result = ''
unit = ''
length = 0

for input in input():
    if input == unit:
        length += 1
    else:
        if length != 0:
            result += unit + str(length)
        # 初期化処理
        unit = input
        length = 1
result += unit + str(length)

print(result)

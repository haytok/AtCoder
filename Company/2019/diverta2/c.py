N = int(input())
inputs = sorted([int(i) for i in input().split()])

min_value = inputs[0]
max_value = inputs[-1]
process = []
for i in range(1, N-1):
    value = inputs[i]
    if value >= 0:
        process.append([min_value, value])
        min_value -= value
    elif value < 0:
        process.append([max_value, value])
        max_value -= value
process.append([max_value, min_value])

print(max_value - min_value)
for item in process:
    print(item[0], item[1])

"""
初めて500点問題を解いたけど、発想が結構重要な問題やった。
実装できない典型的なアルゴリズム以外の問題やと、解けることもあると感じた。
"""

D, G = map(int, input().split())
inputs = [list(map(int, input().split())) for _ in range(D)]

ans = 10 ** 7
for i in range(2 ** D):
    bit = format(i, 'b').zfill(D)
    count = 0
    score = 0
    # ボーナスの分を加算
    for index in range(len(bit)):
        if bit[index] == '1':
            score += 100 * (index + 1) * inputs[index][0] + inputs[index][1]
            count += inputs[index][0]
    if G <= score:
        ans = min(ans, count)
        continue
    
    for j in range(len(bit)-1, -1, -1):
        if bit[j] == '0':
            if G - score <= 100 * (j + 1) * (inputs[j][0] - 1):
                count += (G - score) // (100 * (j + 1)) + (1 if (G - score) % (100 * (j + 1)) != 0 else 0)
                ans = min(ans, count)
                break
            else:
                score += 100 * (j + 1) * (inputs[j][0] - 1)
                count += inputs[j][0] - 1

print(ans)

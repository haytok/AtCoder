inputs = [list(input()) for _ in range(4)]
ans = []

for input in inputs[::-1]:
    element = []
    for i in input[::-1]:
        element.append(i)
    ans.append(element)

for row in ans:
    print(''.join(row))

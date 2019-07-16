import copy

inputs = [list(input()) for i in range(10)]

ans = [['x'] * 10 for _ in range(10)]
vectors = [[0, -1], [-1, 0], [0, 1], [1, 0]]

def dfs(row, col):
    if not(row >= 10 or col >= 10 or row < 0 or col < 0 or copy_inputs[row][col] == 'x'):
        copy_inputs[row][col] = 'x'
        for y, x in vectors:
            dfs(row+y, col+x)

for row in range(10):
    for col in range(10):
        if inputs[row][col] == 'x':
            copy_inputs = copy.deepcopy(inputs)
            copy_inputs[row][col] = 'o'
            dfs(row, col)
            if ans == copy_inputs:
                print('YES')
                exit()
else:
    print('NO')

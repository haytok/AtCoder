N, A, B, C = map(int, input().split())
inputs = [int(input()) for _ in range(N)]

def dfs(depth, a, b, c):
	# 再帰を終了させるための処理
	if depth == N:
		if a == 0 or b == 0 or c == 0:
			ans.append(1e9)
			return 1e9
		return abs(A - a) + abs(B - b) + abs(C - c)

	# xは終了条件で使われてて、深さすなはち何重のfor文を回すかを表現
	x = dfs(depth + 1, a, b, c)
	y = dfs(depth + 1, a + inputs[depth], b, c) + 10 * (a != 0)
	z = dfs(depth + 1, a, b + inputs[depth], c) + 10 * (b != 0)
	w = dfs(depth + 1, a, b, c + inputs[depth]) + 10 * (c != 0)
	
	return min(x, y, z, w)

print(dfs(0, 0, 0, 0))

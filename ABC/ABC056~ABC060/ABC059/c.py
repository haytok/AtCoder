n = int(input())
a = list(map(int,input().split()))

def calc(t):
	global a
	ans = 0
	s = 0
	for i in a:
		s += i
		if s * t <= 0:
			ans += abs(s-t)
			s = t
		t *= -1
	return ans

print(min(calc(1),calc(-1)))

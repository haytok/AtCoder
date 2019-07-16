N, A, B = map(int, input().split())

now = 0

def cal(n):
    if n < A:
        return A
    elif A <= n <= B:
        return n
    elif n > B:
        return B

for _ in range(N):
    direction, distance = input().split()
    if direction == 'East':
        now += cal(int(distance))
    else:
        now -= cal(int(distance))

if now > 0:
    print('East {}'.format(now))
elif now == 0:
    print(0)
else:
    print('West {}'.format(-now))
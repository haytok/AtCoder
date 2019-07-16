N = int(input())

sum = 0
for i in range(1, 10):
    for j in range(1, 10):
        sum += i * j

diff = sum - N

if diff == 1:
    print('1 x 1')
else:
    for i in range(1, 10):
        if diff % i == 0 and (1 <= diff // i <= 9):
            print('{} x {}'.format(i, diff // i))

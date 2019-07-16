N = int(input())
A, B = map(int, input().split())

a, b, c = 0, 0, 0

for i in input().split():
    item = int(i)
    if item <= A:
        a += 1
    elif A + 1 <= item <= B:
        b += 1
    elif B < item:
        c += 1

print(min(a, b, c))

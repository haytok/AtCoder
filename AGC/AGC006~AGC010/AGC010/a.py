N = int(input())

even = 0

for i in input().split():
    if int(i) % 2 != 0:
        even += 1

print('NO' if even % 2 == 1 else 'YES')

result = 0

for _ in range(3):
    a, b = map(int, input().split())
    result += a * b // 10

print(result)

# print(sum([eval(input().replace(' ', '*')) for _ in range(3)])//10)
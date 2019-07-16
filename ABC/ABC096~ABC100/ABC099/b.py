a, b = map(int, input().split())

result = 0

for i in  range(1,b-a):
    result += i

print(result-a)
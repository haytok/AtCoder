N = int(input())
items = ['1', '2', '3', '4', '5', '6']

for n in range(N % 30):
    items[n % 5], items[n % 5 + 1] = items[n % 5 + 1], items[n % 5]

print(''.join(items))

N = int(input())
inputs = input()

print(sum([(69 - ord(i)) * inputs.count(i) for i in 'ABCD']) / N)

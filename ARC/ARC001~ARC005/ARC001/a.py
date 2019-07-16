N = int(input())
C = input()

counts = [C.count(str(i)) for i in range(1, 5)]

print(max(counts), min(counts))

from collections import Counter

N = int(input())

index = 0
even_numbers = []
odd_numbers = []

for i in input().split():
    if index % 2 == 0:
        even_numbers.append(int(i))
    else:
        odd_numbers.append(int(i))
    index += 1

even = Counter(even_numbers).most_common(2)
odd = Counter(odd_numbers).most_common(2)

if even[0][0] == odd[0][0]:
    if len(even) == 1:
        print(N//2)
    else:
        print(N - even[0][1] - max(even[1][1], odd[1][1]))
else:
    print(N - even[0][1] - odd[0][1])

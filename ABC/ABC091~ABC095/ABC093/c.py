data = [int(i) for i in input().split()]
data.sort()
count = 0

if (data[1] - data[0]) % 2 == 1:
    data[1] += 1
    data[2] += 1
    count += 1
count += int((data[1] - data[0]) / 2) + (data[2] - data[1])

print(count)
K, S = map(int, input().split())

count = 0

for z in range(K, -1, -1):
    for y in range(K, -1, -1):
        x = S - z - y
        if z >= y and y >= x and x >= 0:
            if x == y == z:
                count += 1
            elif (x == y and y != z) or (y == z and z != x):
                count += 3
            else:
                count += 6

print(count)

# K,S = (int(i) for i in input().split())

# count = 0
# for i in range(K+1):
#     for j in range(K+1):
#         X = i
#         Y = j
#         Z = S-X-Y
#         if(Z<=K and Z>=0):
#             count = count + 1

# print(count)

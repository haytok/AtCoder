N = int(input())
input_list = [int(i) for i in input().split()]
four_count = 0
two_count = 0

for i in input_list:
    if i % 4 == 0:
        four_count += 1
    elif i % 2 == 0:
        two_count += 1

others_count = N - four_count - two_count

if two_count:
    if others_count <= four_count:
        print("Yes")
    else:
        print("No")
else:
    if others_count <= four_count + 1:
        print("Yes")
    else:
        print("No")
    
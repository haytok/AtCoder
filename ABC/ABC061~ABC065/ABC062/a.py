x, y = map(int, input().split())

group_1 = set([1, 3, 5, 7, 8, 10, 12])
group_2 = set([4, 6, 9, 11])
group_3 = set([2])

# orを使えばif文をまとめられるよね
if x in group_1 and y in group_1:
    print("Yes")
elif x in group_2 and y in group_2:
    print("Yes")
else:
    print("No")
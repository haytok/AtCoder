list = list(int(i) for i in input().split())
count = 0

for i in range(list[0], list[1]+1):
    if str(i)[0] == str(i)[4] and str(i)[1] == str(i)[3] :
        count += 1
print(count)
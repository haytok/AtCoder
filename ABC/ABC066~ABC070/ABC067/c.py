N = int(input())
input_list = [int(i) for i in input().split()]

index = 1
ruiseki_list = [0]*(N+1)
result = 10*9

if N == 2:
    print(abs(input_list[0]-input_list[1]))
else:
    for i in input_list:
        ruiseki_list[index] = ruiseki_list[index-1] + i
        index += 1

    mapped_list = map(lambda x: ruiseki_list[N]-x, ruiseki_list)
    result_list = [abs(a-b) for (a, b) in zip(ruiseki_list, mapped_list)]
    print(min(result_list[2:N]))
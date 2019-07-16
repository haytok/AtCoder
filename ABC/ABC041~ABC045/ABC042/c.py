N, K = map(int, input().split())
inputs_set = set([i for i in input().split()])

all_set = set({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})
rest_set = all_set - inputs_set

for i in range(N, N*10 + 1):
    if set(str(i)) <= rest_set:
        print(i)
        break
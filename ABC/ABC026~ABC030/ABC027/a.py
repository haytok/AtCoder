inputs = list(map(int, input().split()))

if len(set(inputs)) == 1:
    print(inputs[0])
else:
    for i in set(inputs):
        if inputs.count(i) == 1:
            print(i)

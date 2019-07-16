set_S = set(list(input()))

if len(set_S) == 2:
    if set_S == set(['N', 'S']):
        print('Yes')
    elif set_S == set(['W', 'E']):
        print('Yes')
    else:
        print('No')
elif len(set_S) == 4:
    print('Yes')
else:
    print('No')

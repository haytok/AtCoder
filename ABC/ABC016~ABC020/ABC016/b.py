A, B, C = map(int, input().split())

add = A + B
sub = A - B

if add == C and sub == C:
    print('?')
elif add == C:
    print('+')
elif sub == C:
    print('-')
else:
    print('!')
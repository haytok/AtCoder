A = list(input())
B = list(input())
C = list(input())

owner = 'a'

while True:
    if owner == 'a':
        if len(A):
            owner = A[0]
            del(A[0])
        else:
            print('A')
            break
    if owner == 'b':
        if len(B):
            owner = B[0]
            del(B[0])
        else:
            print('B')
            break
    if owner == 'c':
        if len(C):
            owner = C[0]
            del(C[0])
        else:
            print('C')
            break
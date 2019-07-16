N = input()
A = int(N[0])
B = int(N[1])
C = int(N[2])
D = int(N[3])

while True:
    if A + B + C + D == 7:
        print(str(A) + "+" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
        break
    elif A + B + C - D == 7:
        print(str(A) + "+" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
        break
    elif A + B - C + D == 7:
        print(str(A) + "+" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
        break
    elif A + B - C - D == 7:
        print(str(A) + "+" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
        break
    elif A - B + C + D == 7:
        print(str(A) + "-" + str(B) + "+" + str(C) + "+" + str(D) + "=7")
        break
    elif A - B - C + D == 7:
        print(str(A) + "-" + str(B) + "-" + str(C) + "+" + str(D) + "=7")
        break
    elif A - B + C - D == 7:
        print(str(A) + "-" + str(B) + "+" + str(C) + "-" + str(D) + "=7")
        break
    elif A - B - C - D == 7:
        print(str(A) + "-" + str(B) + "-" + str(C) + "-" + str(D) + "=7")
        break
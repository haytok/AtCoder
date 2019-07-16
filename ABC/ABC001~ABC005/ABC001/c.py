A, B = map(int, input().split())

def cal_A(a):
    const = 11.25
    if const <= a < const * 3:
        return 'NNE'
    elif const * 3 <= a < const * 5:
        return 'NE'
    elif const * 5 <= a < const * 7:
        return 'ENE'
    elif const * 7 <= a < const * 9:
        return 'E'
    elif const * 9 <= a < const * 11:
        return 'ESE'
    elif const * 11 <= a < const * 13:
        return 'SE'
    elif const * 13 <= a < const * 15:
        return 'SSE'
    elif const * 15 <= a < const * 17:
        return 'S'
    elif const * 17 <= a < const * 19:
        return 'SSW'
    elif const * 19 <= a < const * 21:
        return 'SW'
    elif const * 21 <= a < const * 23:
        return 'WSW'
    elif const * 23 <= a < const * 25:
        return 'W'
    elif const * 25 <= a < const * 27:
        return 'WNW'
    elif const * 27 <= a < const * 29:
        return 'NW'
    elif const * 29 <= a < const * 31:
        return 'NNW'
    else:
        return 'N'

def cal_B(b):
    if 0 <= b < 0.25:
        return 0
    elif 0.25 <= b < 1.55:
        return 1
    elif 1.55 <= b < 3.35:
        return 2
    elif 3.35 <= b < 5.45:
        return 3
    elif 5.45 <= b < 7.95:
        return 4
    elif 7.95 <= b < 10.75:
        return 5
    elif 10.75 <= b < 13.85:
        return 6
    elif 13.85 <= b < 17.15:
        return 7
    elif 17.15 <= b < 20.75:
        return 8
    elif 20.75 <= b < 24.45:
        return 9
    elif 24.45 <= b < 28.45:
        return 10
    elif 28.45 <= b < 32.65:
        return 11
    elif 32.65 <= b:
        return 12

ans_A = cal_A(A/10)
ans_B = cal_B(B/60)

print('C' if int(ans_B) == 0 else ans_A, ans_B)

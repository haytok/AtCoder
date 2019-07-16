m = int(input()) # 単位はメートル

vv = '00'

if 100 <= m <= 5000:
    km = m // 100
    if 1 <= km <= 9:
        vv = '0' + str(km)
    else:
        vv = str(km)
elif 6000 <= m <= 30000:
    vv = int(m/1000 + 50)
elif 35000 <= m <= 70000:
    vv = str(int((m/1000 - 30) / 5) + 80)
elif m > 70000:
    vv = '89'

print(vv)

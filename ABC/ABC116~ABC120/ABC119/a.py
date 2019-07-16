yy, mm, dd = input().split('/')

last_yy, last_mm, last_dd = '2019/04/30'.split('/')

print('Heisei' if last_yy >= yy and last_mm >= mm and last_dd >= dd else 'TBD')

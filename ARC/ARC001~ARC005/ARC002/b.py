from datetime import datetime, timedelta

ans = input()

add = timedelta(days=1)
while True:
    year, month, day = map(int, ans.split('/'))

    if year % month == 0 and (year // month) % day == 0:
        print(ans)
        break
    
    nexd_day = datetime.strptime(ans, '%Y/%m/%d') + add
    ans = nexd_day.strftime('%Y/%m/%d')

y = int(input())
m = int(input())
d = int(input())

def cal(y, m, d):
    return 365 * y + y // 4 - y // 100 + y // 400 + 306 * (m + 1) // 10 + d - 429

ans = 0
if m == 1 or m == 2:
    y -= 1
    m += 12

print(cal(2014, 5, 17) - cal(y, m, d))

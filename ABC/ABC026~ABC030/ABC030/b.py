n, m = map(int, input().split())

n = n - 12 if n > 12 else n

short = 30 * n + m * 0.5
long = 6 * m
dgree = abs(long - short)

print(min(float(360)-dgree, dgree))

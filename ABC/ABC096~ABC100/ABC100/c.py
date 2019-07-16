N = int(input())
List = list(int(i) for i in input().split())
count = 0

def cal(n):
    count = 0
    while True:
        if n % 2 == 0:
            count += 1
            n /= 2
        else:
            break
    return count

for i in List:
    count += cal(i)

print(count)

# 俺が書けへんのスクリプトを拝めた
# input()
# print(sum(bin(x)[::-1].index('1')for x in map(int,input().split())))

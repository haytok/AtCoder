N = int(input())

def cal(x):
    x = int(x)
    while True:
        if x % 2 == 0:
            x //= 2
        else:
            return x 

result = set(map(cal, input().split()))

print(len(result))

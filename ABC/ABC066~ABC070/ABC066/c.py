from collections import deque

n = int(input())

result = deque()
index = 0

def front_enque(i):
    global result, index
    result.appendleft(i)
    index += 1

def enque(i):
    global result, index
    result.append(i)
    index += 1

if n % 2 == 0:
    for i in input().split():
        if index % 2 == 1:
            front_enque(i)
        else:
            enque(i)
else:
    for i in input().split():
        if index % 2 == 1:
            enque(i)
        else:
            front_enque(i)

print(" ".join(result))
N = int(input())
list = list(int(i) for i in input().split())
list.insert(0, 0)
list.insert(N+1, 0)
total = 0


for i in range(N+1):
    total += abs(list[i]-list[i+1])
for i in range(N):
    print(total - abs(list[i+1]-list[i+2]) - abs(list[i]-list[i+1]) + abs(list[i]-list[i+2]))
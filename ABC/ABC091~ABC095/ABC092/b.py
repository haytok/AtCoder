N = int(input())
D, X = map(int, input().split())
List = [int(input()) for i in range(N)] 

count = 0

for n in range(N):
    count += (1 + (D-1) // List[n])

print(count + X)
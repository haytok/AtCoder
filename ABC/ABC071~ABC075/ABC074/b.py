N = int(input())
K = int(input())
X = list(int(i) for i in input().split())

distance = 0

for i in X:
    distance += min(i*2, (K-i)*2)
    
print(distance)

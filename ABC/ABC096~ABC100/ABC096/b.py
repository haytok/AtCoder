List = [int(i) for i in input().split()]
K = int(input())

maxNumber = max(List)
List.remove(maxNumber)

print(maxNumber* pow(2, K) + List[0] + List[1])

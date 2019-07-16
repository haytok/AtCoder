A, B, C = map(int, input().split())

total = A * B * C

print(total // max(A, B, C) if total % 2 != 0 else 0)

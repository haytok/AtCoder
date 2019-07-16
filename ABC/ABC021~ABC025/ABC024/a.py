A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

no_discount = A * S + B * T

print(no_discount if S + T < K else no_discount - C * (S + T))
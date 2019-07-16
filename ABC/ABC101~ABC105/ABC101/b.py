N = input()
sum = 0

for i in range(len(N)):
    sum += int(N[i])

print("Yes" if int(N) % sum == 0 else "No")

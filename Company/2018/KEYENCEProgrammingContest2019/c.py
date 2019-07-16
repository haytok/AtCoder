N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()] # 必要な準備

needs = []
need = 0
ans = 0
if sum(A) < sum(B):
    ans = -1
else:
    for i in range(N):
        diff = A[i] - B[i]
        if diff < 0:
            ans += 1
            need += (-diff)
        elif diff > 0:
            needs.append(diff)
    if need != 0:
        needs.sort(reverse=True)
        for item in needs:
            need -= item
            ans += 1
            if need <= 0:
                break

print(ans)

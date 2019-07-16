S = input()
T = int(input())

question_count = S.count('?')
ans = abs(S.count('R') - S.count('L')) + abs(S.count('U') - S.count('D'))

if T == 1:
    ans += question_count
else:
    if ans <= question_count:
        ans = (question_count - ans) % 2
    else:
        ans -= question_count

print(ans)
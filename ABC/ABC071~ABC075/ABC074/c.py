A, B, C, D, E, F = map(int, input().split())

def cal():
    answer = (100*A, 0)
    for a in range(0, F, 100*A):
        for b in range(0, F, 100*B):
            for c in range(0, F, C):
                for d in range(0, F, D):
                    water, sugar = a + b, c + d
                    if water == 0 or water + sugar > F or 100*sugar > E*water :
                        break
                    elif 100*sugar == E*water:
                        return (water, sugar)
                    elif answer[1]*water < sugar*answer[0]:
                        answer = (water, sugar)
    return answer

answer = cal()

print(sum(answer), answer[1])

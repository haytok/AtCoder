def solution(X, Y, D):
    diff = Y - X
    ans = diff // D 
    ans += 1 if diff  % D != 0 else 0
    return ans

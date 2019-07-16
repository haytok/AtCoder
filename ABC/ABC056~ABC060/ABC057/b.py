N, M = map(int, input().split())
n_list = [[int(i) for i in input().split()] for i in range(N)] 
m_list = [[int(i) for i in input().split()] for i in range(M)] 

# 距離を計算する関数
def cal_distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for n in n_list:
    distance = 10 ** 16
    ans = 0
    for i in range(len(m_list)):
        this_distance = cal_distance(n[0], m_list[i][0], n[1], m_list[i][1])
        if distance > this_distance:
            distance = this_distance
            ans = (i + 1)
    print(ans)

# n,m = map(int,input().split())
# ab = [list(map(int,input().split())) for x in [0]*n]
# cd = [list(map(int,input().split())) for x in [0]*m]
# for a,b in ab:
#     # この下２行が超上手い。
#     # 俺が６行もかかったのを２行でやってのけるのはすごい。
#     # indexが欲しいから、listに計算結果全てを突っ込んで、
#     # その中から、最小値のindexを取った
#     l = [abs(a-c)+abs(b-d) for c,d in cd]
#     print(l.index(min(l))+1)

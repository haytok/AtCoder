# def rotate(S, N):
#     rotated_S = []
#     for i in range(N):
#         tmp_s = ''
#         for j in range(N-1, -1, -1):
#             tmp_s += S[j][i]
#         rotated_S.append(tmp_s)

#     return rotated_S

# def move(S, N):
#     moved_S = []
#     for i in range(N):
#         moved_S.append(S[i][1:]+S[i][:1])
#     return moved_S

# def main():
#     N = int(input())
#     S = []
#     T = []
#     for _ in range(N):
#         S.append(input())
#     for _ in range(N):
#         T.append(input())
    
#     print(T)
#     print('----------')
#     for i in range(4):
#         tmp_s = S
#         for _ in range(N):
#             if i == 3:
#                 print('\n'.join(S))
#                 print('----')
#             S = move(S, N)
#             if S == T:
#                 print('Yes')
#                 return
#         S = rotate(S, N)
    
#     print('No')

# if __name__ == '__main__':
#     main()

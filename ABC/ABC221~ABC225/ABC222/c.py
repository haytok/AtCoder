def orig_sort(rank):
    rank = sorted(rank, key=lambda item: item['number'])
    rank = sorted(rank, key=lambda item: item['score'], reverse=True)
    return rank

def add_score(rank, n):
    for i in range(len(rank)):
        if rank[i]['number'] == n:
            rank[i]["score"] += 1

def main():
    N, M = map(lambda s: int(s), input().split(' '))
    results = [input() for _ in range(N*2)]
    rev_results = []
    for m in range(M):
        rev_results.append(''.join([results[n][m] for n in range(N*2)]))

    rank = [{'number': i+1, 'score': 0} for i in range(N*2)]
    
    for m in range(M):
        for k in range(1, N+1):
            i_0, i_1 = 2 * k - 1, 2 * k
            # 1 位と 2 位、3 位と 4 位が出した手を確認する。
            a, b = rank[i_0-1]['number'] - 1, rank[i_1-1]['number'] - 1
            i_0_result, i_1_result = rev_results[m][a], rev_results[m][b]
            if (i_0_result == 'G' and i_1_result == 'C') or (i_0_result == 'C' and i_1_result == 'P') or (i_0_result == 'P' and i_1_result == 'G'):
                # i_0 の勝ち
                add_score(rank, a+1)
            elif (i_0_result == 'G' and i_1_result == 'P') or (i_0_result == 'C' and i_1_result == 'G') or (i_0_result == 'P' and i_1_result == 'C'):
                # i_1 の勝ち
                add_score(rank, b+1)
            else:
                continue
        rank = orig_sort(rank)

    for r in rank:
        print(r['number'])

if __name__ == '__main__':
    main()

def parse(string):
    dna = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    return dna[string]

def solution(S, P, Q):
    data = [[0] * 4] * (len(S) + 1)
    for index, string in enumerate(S):
        # list()にしないと参照でバグる
        data[index+1] = list(data[index])
        dna_index = parse(string)
        data[index+1][dna_index] += 1
    ans = []
    for p, q in zip(P, Q):
        p_data, q_data = data[p], data[q+1]
        print('p, q', p, q, p_data, q_data)
        for diff_index in range(4):
            diff = q_data[diff_index] - p_data[diff_index]
            if diff != 0:
                ans.append(diff_index + 1)
                break
    return ans

if __name__ == '__main__':
    S, P, Q = 'CAGCCTA', [2, 5, 0], [4, 5, 6]
    # S, P, Q = 'CAGCCTA', [0, 0, 0], [0, 0, 0]
    print(solution(S, P, Q))
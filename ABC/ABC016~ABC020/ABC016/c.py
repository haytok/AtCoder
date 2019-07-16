N, M = map(int, input().split())

relations = [set([i]) for i in range(N)]

for m in range(M):
    A, B = map(int, input().split())
    relations[A-1].add(B-1)
    relations[B-1].add(A-1)

for relation in relations:
    friend = set()
    for r in relation:
        friend |= relations[r]
    print(len(friend - relation))
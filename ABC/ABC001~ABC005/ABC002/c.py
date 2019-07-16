ax, ay, bx, by, cx, cy = map(int, input().split())

vector_ab = [bx-ax, by-ay]
vector_ac = [cx-ax, cy-ay]

print(abs(vector_ab[0] * vector_ac[1] - vector_ac[0] * vector_ab[1]) / 2)

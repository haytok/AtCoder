"""
入力
N = 10, M = 10

#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#

出力
"""

H, W = map(int, input().split())
inputs = [list(input()) for i in range(H)]

vectors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for h in range(H):
    if 'S' in item:
        start_h, start_w = h, item.index('S')
    elif 'G' in item:
        goal_h, goal_w = h, item.index('G')

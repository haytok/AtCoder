W, H = map(int, input().split())

print('4:3' if (W // 4 * 3) == H else '16:9')
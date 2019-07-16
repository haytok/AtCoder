import math
import numpy as np

H, W = map(int, input().split())

result = 10**10

def vertical_and_horizontal_cal(h, w):
    global result
    # - | このパターンを検証中
    for i in range(1, math.ceil(h / 2) + 1):
        area = np.array([i * w, (h-i) * (w//2), (h-i) * (w - w//2)])
        result = min(result, max(area) - min(area))

def vertical_and_vertical_cal(h, w):
    global result
    # - - このパターンを検証中
    for i in range(1, math.ceil(h / 2) + 1):
            area = np.array([i * w,  ((h-i)//2) * w, (h - i - (h-i)//2) * w])
            result = min(result, max(area) - min(area))


vertical_and_horizontal_cal(H, W)
vertical_and_horizontal_cal(W, H)
vertical_and_vertical_cal(H, W)
vertical_and_vertical_cal(W, H)

print(result)

sx, sy, tx, ty = map(int, input().split())

yu = "U" * (ty - sy)
xr = "R" * (tx - sx)
yd = "D" * (ty - sy)
xl = "L" * (tx - sx)

print(yu + xr + yd + xl + "L" + yu + "U" + xr + "R" + "D" + "R" + yd + "D" + xl + "L" + "U")

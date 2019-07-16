List = list(int(i) for i in input().split())

if abs(List[0]-List[2]) <= List[3] :
    print('Yes')
elif (abs(List[0]-List[1]) <= List[3]) and (abs(List[1]-List[2]) <= List[3]) :
    print('Yes')
else:
    print('No')
def solution(line):
    xlist = []
    ylist = []
    answer = []
    start_points=[]
    
    for i in range(len(line)):           # 첫번쨰 직선
        a, b, e = line[i]
        for j in range(i, len(line)):    # 두번쨰 직선
            c, d, f = line[j]
            adbc = (a*d-b*c)
            if adbc==0: continue    # 평행 or 일치
            x = (b*f-e*d)/adbc
            y = (e*c-a*f)/adbc
            if (x.is_integer() and y.is_integer()):
                start_points.append((int(x),int(y)))
                xlist.append(int(x))
                ylist.append(int(y))
                
    
    # x크기, y크기 구하기
    max_x,min_x = max(xlist),min(xlist)
    max_y,min_y = max(ylist),min(ylist)
    x_size = max_x - min_x + 1
    y_size = max_y - min_y + 1
    
    arr= [['.'] * x_size for _ in range(y_size)]
    for x,y in start_points:
        arr[max_y-y][x-min_x] = '*'
        
    return [''.join(s) for s in arr]

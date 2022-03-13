n = int(input())
for i in range(n) :
    lo = list(map(int,input().split()))
    r = ((lo[3]-lo[0])**2 + (lo[4]-lo[1])**2)**0.5
    if r == 0 :
        if lo[2] == lo[5] :
            print(-1)
        else :
            print(0)
    else :
        if (r == (lo[2] + lo[5])) or r == abs(lo[2] - lo[5]) :
            print(1)
        elif (r < (lo[2] + lo[5])) and (r > abs(lo[2] - lo[5])) :
            print(2)
        else :
            print(0)   
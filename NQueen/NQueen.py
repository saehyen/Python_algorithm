N = int(input())
map = [[1] * N for i in range(N)]
for i in range(N) :
    for j in range(N) :
        if map[i][j] == 1 :
            # 가로 세로
            for k in range(i+1,N) :
                map[k][j] = 0
            for l in range(j+1,N) :
                map[i][l] = 0
            # 대각선
            a,b = i,j
            while(a<N-1 and b<N-1) :
                a,b = a+1,b+1
                map[a][b] = 0
print(map)
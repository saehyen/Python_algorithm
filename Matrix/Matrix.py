N,M = map(int,input().split())
cnt=0
change_maps = [list(map(int,input())) for _ in range(N)]
result_maps = [list(map(int,input())) for _ in range(N)]

# 바꾸는 함수 정의
def convert(x,y,arr) :
    for i in range(x,x+3):
        for j in range(y,y+3) :
            change_maps[i][j] = 1 - change_maps[i][j]

# 3x3 범위내 검사했을때 맞지 않으면 change
# 중심점의 좌표를 1,1로 잡는것이 아닌 0,0으로 잡는것이 핵심
for i in range(0,N-2) :
    for j in range(0,M-2) :
        if change_maps[i][j] != result_maps[i][j] :
            convert(i,j,change_maps)
            cnt += 1

# 끝까지 바꿔도 같지않다면 nonlst = True
nonlst = False
for i in range(0,N):
    for j in range(0,M) :
        if change_maps[i][j] != result_maps[i][j]:
            nonlst = True

# 끝까지 바꿔도 같지 않으면 -1 출력
if(nonlst):
    print(-1)
# 아닐경우 결과값 출력
else :
    print(cnt)
n,m = map(int,input().split())

# n * m 맵을 0으로 초기화해서 생성
d = [[0] * m for _ in range(n)]

x,y,direction = map(int,input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 맵 정보 입력받기
array = []
for i in range(n) :
    array.append(list(map(int,input().split())))

# 북 동 남 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left() :
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True :
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 갈수있는 칸이 없는 경우
    else :
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else :
            break
        turn_time = 0

print(count)
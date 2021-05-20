# 데이터 입력받기
n = int(input())
x,y = 1,1
plans = input().split()

# L R U 에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획 확인
for plan in plans :
    for i in range(len(move_types)) :
        nx = x + dx[i]
        ny = y + dy[i]

    # 예외사항 처리
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
# 이동
    x,y = nx,ny

print(x,y)
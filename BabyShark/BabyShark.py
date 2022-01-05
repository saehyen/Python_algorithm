from collections import deque
n = int(input())
maplist = []
# 상하좌우
dxs = [-1,0,0,1]
dys = [0,-1,1,0]

def check_map(shark):
    for i in range(n):
        for j in range(n):
            if maplist[i][j] != 0 and maplist[i][j] < shark:
                return True
    return False

def bfs(x, y):
    q, visited = deque([(x, y)]), set([(x, y)])
    time = 0
    shark = 2  # 아기 상어 크기.
    eat = 0    # 지금까지 먹은 물고기 수다.
    eat_flag = False # for _ in range(size) 구문을 진행하지 않기 위한 플래그다.

    while q:
        size = len(q)

        # 위, 그리고 왼쪽을 더 우선시해서 가야하기 때문에, BFS queue를 소팅해준다.
        q = deque(sorted(q))
        for _ in range(size):
            x, y = q.popleft()

            # 현재 위치에 아기 상어보다 작은 물고기가 있어서, 이를 먹은 경우.
            if maplist[x][y] != 0 and maplist[x][y] < shark:
                maplist[x][y] = 0
                eat += 1

                # 아기 상어의 크기 만큼 먹었다면, 아기 상어의 크기를 +1 해줘야한다.
                if eat == shark:
                    shark += 1
                    eat = 0               

                # 먹고 난 뒤, 현재 판에 더 먹을게 있는지 확인하고 없으면 현재 스텝을 반환한다.
                if not check_map(shark):
                    return time

                # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처를 탐색해야 하기 때문에,
                # BFS queue 와 visited 를 초기화 해준다.
                q, visited = deque(), set([(x, y)])
                eat_flag = True

            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < n and (nx, ny) not in visited:
                    if maplist[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            # 현재 위치에서 먹었다면, 더 이상 위 반복문을 돌 필요가 없다.
            if eat_flag:
                eat_flag = False
                break

        time += 1
    return time

for i in range(n):
    temp = list(map(int,input().split()))
    maplist.append(temp)

s_x, s_y = None, None
for i in range(n):
    for j in range(n):
        if maplist[i][j] == 9:
            s_x, s_y = i, j
            maplist[i][j] = 0

if check_map(2):
    print(bfs(s_x, s_y))
else:
    print(0)
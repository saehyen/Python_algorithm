# bfs
from collections import deque
N,M = map(int,input().split())
dx,dy= [1,2,2,1],[2,1,-1,-2]
graph =  [[0] for M in range(M) for n in range(N)]

# bfs 셋팅
def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

# ... 이 풀이 아닌 듯하여 변경
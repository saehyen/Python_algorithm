# DFS
# 재귀함수 사용
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    # 벽 규정
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    # 전역변수 count
    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        # 4방향 모두 재귀함수
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0
# 이 문제의 핵심
for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])
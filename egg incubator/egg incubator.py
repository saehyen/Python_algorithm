# 정답
from collections import deque
M, N = map(int, input().split())

maps = []
start = []
for y in range(N):
	temp = list(map(int, input().split()))
	for x in range(M):
		if temp[x] == 1:
            # 스타팅 지점 추가
			start.append((y, x, 0))
	maps.append(temp)

def bfs(start, maps):
	queue = deque()
	queue.extend(start)
	dirs = [(0,1),(0,-1),(1,0),(-1,0)]

	# 처음부터 '부화한 달걀' 이 없을 경우 == -1 반환
	if not queue:
		return -1
	while queue:
		y, x, cnt = queue.popleft()
		for dy, dx in dirs:
			ny, nx = y + dy, x + dx
            # 범위 내에 존재할 경우
			if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
				if maps[ny][nx] == 0:
					maps[ny][nx] = 1
					queue.append((ny, nx, cnt+1))
	return cnt

def is_zero(maps):
	for y in range(N):
		if maps[y].count(0) != 0:
			return True
	return False


answer = bfs(start, maps)

# 달걀이 부화하지 못한 게 하나라도 남아 있을 경우
if is_zero(maps):
	print(-1)
else:
	print(answer)
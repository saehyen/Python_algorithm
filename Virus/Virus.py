n = int(input())
m = int(input())
# graph 
graph = [[]*n for _ in range(n+1)]
# 경로 추가
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# 그래프 확인    
# print(graph)
# cnt : 정답
cnt = 0
visited = [0]*(n+1)

def dfs(start):
    global cnt
    visited[start] = 1
    # 방문되지 않았으면 cnt+1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
# 출발지 : 1
dfs(1)
print(cnt)
# 재귀함수로 풀이 진행중
import sys
sys.setrecursionlimit(10**7)
# 현재 돈, 인덱스
def dfs(N,money,idx,table):
    global max_m
    # 돈 더해주기
    money += table[idx][1]
    max_m = max(max_m,money)
    # 뒤에 모든 일정에 관하여 재귀함수
    if idx < N :
        for i in range(idx,N):
            dfs(N,money,i,table)
    money += table[idx][1]

N = int(input())
table = []
for i in range(N):
    a,b = map(int,input().split())
    table.append([a,b])
print(table)

max_m = 0
dfs(N,0,0,table)
print(max_m)
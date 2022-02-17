# 1차시도
import itertools
# 능력치 총합 구해주는 함수
def sumab(maps,startteam,linkteam):
    starttotal = 0
    linktotal = 0
    team = startteam
    for j in team:
        for k in team:
            starttotal += maps[j][k] #멤버와 함께할 경우의 능력치들

    team = linkteam
    for j in team:
        for k in team:
            linktotal += maps[j][k] #멤버와 함께할 경우의 능력치들
    return abs(starttotal-linktotal)

# 능력치 맵 가져오기
n = int(input())
maps = []
for i in range(n) :
    tmp = list(map(int,input().split()))
    maps.append(tmp)

# 팀 나누기
arr = list(range((n)))
startteam = []
for team in list(itertools.combinations(arr, n//2)):
    startteam.append(list(team))

# 최솟값 비교하기
minab = 1000000
for i in range(len(startteam)//2):
    minab = min(minab,sumab(maps,list(startteam[i]),list(startteam[-i-1])))
print(minab)
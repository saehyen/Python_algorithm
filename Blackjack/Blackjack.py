from itertools import combinations, permutations
N,M = map(int,input().split())
cardlist=list(map(int,input().split()))
cardlist.sort()
ans = 0
iterlist = list(combinations(cardlist,3))
for i in range(len(iterlist)):
    if sum(iterlist[i]) <= M and ans < sum(iterlist[i]):
        ans = sum(iterlist[i])
    else :
        continue
print(ans)
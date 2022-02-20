from itertools import combinations
N,S = map(int,input().split())
ans = 0
nums = list(map(int,input().split()))
for j in range(1,len(nums)+1) :
    for i in combinations(nums,j):
        if sum(i) == S :
            ans += 1
print(ans)

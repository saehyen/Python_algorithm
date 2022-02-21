from itertools import combinations
L,C = map(int,input().split())
alphabats = list(map(str,input().split()))
alphabats.sort()
comb = combinations(alphabats,L)
gather = ['a','e','i','o','u']
res = []
for c in comb :
    j = 0
    m = 0
    for i in range(L):
        if c[i] in gather:
            m+= 1
        else :
            j += 1
    if m>=1 and j>= 2:
        print(''.join(c))
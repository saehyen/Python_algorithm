M = int(input())
for i in range(M):
    N = int(input())
    logs = list(map(int,input().split()))
    logs.sort()
    result = 0
    for j in range(2,N):
        result=max(result,abs(logs[j]-logs[j-2]))
    print(result)
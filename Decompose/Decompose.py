M = int(input())
# 1씩 빼가면서 확인
def remain(N) :
    ans = N 
    while (N != 0):
        ans += N % 10
        N = N // 10
    return ans
targetnum = M
answer = 0  
for _ in range(targetnum) :
    targetnum-= 1
    if remain(targetnum) == M :
        answer = targetnum
print(answer)
    
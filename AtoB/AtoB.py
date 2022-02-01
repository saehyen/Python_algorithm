A,B = map(int,input().split())
answer = 0
while(A < B):
    # 1의자리가 1이면 1 제거
    if (str(B)[-1] == '1'):
        B = B // 10
        answer += 1
    # 2로 나누어지면 %2
    elif((B%2) == 0):
        B = B//2
        answer += 1
    # 그 외의 경우 만들기 불가
    else :
        break

if A==B:
    print(answer+1)
else :
    print(-1)
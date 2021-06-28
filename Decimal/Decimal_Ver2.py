# 일반적인 소수만들기 ( 시간초과 )
def solution(n):
    answer = 0
    if n == 2 :
        return 1
    else :
        for i in range(2,n+1):
            # 소수인지 체크하고 answer +1
            for j in range(2,i-1) :
                if i % j == 0:
                    break
            else :
                answer +=1
    return answer
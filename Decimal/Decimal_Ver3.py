# 소수 집합 만들기( 시간초과 )
def solution(n):
    sosus = []
    for i in range(2,n+1):
        for sosu in sosus:
            if i % sosu == 0:
                break
        else :
            sosus.append(i)
    return len(sosus)
# 최대공약수,최소공배수 복잡하지만 보기쉬운 답
def solution(n, m):
    if n<m :
        min = n
        max = m
    elif n==m :
        return [n,m]
    else :
        min = m
        max = n
    for i in range(min+1,1,-1):
        if n%i == 0 and m %i==0:
            res = i
            break
        else :
            res = 1
    lcm = n/res*m
    return [res,lcm]
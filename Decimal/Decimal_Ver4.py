# 에라토스테네스의 체를 이용한 풀이 ( 정답 )
def solution(n):
    num = set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num -= set(range(2*i,n+1,i))
    return len(num)
# 나의 풀이
def solution(n):
    answer = 0
    for i in range(n) :
        num = 0
        j = i+1
        while num<n :
            num += j
            j += 1
        if num == n :
            answer += 1
    return answer
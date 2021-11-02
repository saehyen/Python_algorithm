def solution(n):
    answer = 0
    n1 = 0
    n2 = 1
    for i in range(n-1):
        answer = n1 + n2
        n1 = n2
        n2 = answer
    return answer % 1234567
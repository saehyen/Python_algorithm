def solution(n, left, right):
    answer = []
    
    for i in range(left, right+1):
        # 몫과 나머지 중 최대값 + 1 
        answer.append(max(divmod(i, n)) + 1)

    return answer
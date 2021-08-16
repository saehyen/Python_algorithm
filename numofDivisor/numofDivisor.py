def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        yaksu = 0
        for j in range(1, i + 1):
            if i % j == 0:
                yaksu += 1
        if yaksu % 2 == 0:
            answer += i
        elif yaksu % 2 == 1:
            answer -= i

    return answer
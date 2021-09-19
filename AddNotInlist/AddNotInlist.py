def solution(numbers):
    numbers.sort()
    answer = 0
    numlist = [i for i in range(10)]
    for num in numlist :
        if num not in numbers :
            answer += num
    return answer
def solution(nums):
    # itertools라는 라이브러리에 3가지수를 뽑아주는 것이 있음.
    from itertools import combinations as cb
    answer = 0
    # for 문을 모두 실행하였음에도 break가 걸리지 않는다면 answer+1
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
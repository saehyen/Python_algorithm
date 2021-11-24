def solution(n):
    # 3보다 작으면 1,2,4 중에 하나 선택
    if n <= 3:
        return '124'[n-1]
    else :
        # 3진법 처리하듯이
        # q = 몫 r = 나머지
        q,r = divmod(n-1,3)
        return solution(q) + '124'[r]
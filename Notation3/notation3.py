# divmod 사용 답
# 진법으로 바꾸는 함수 : int(string,N)
# divmod = (n을 3으로 나눈 나머지)
def solution(n):
    answer = ''
    # 1 이상일 때
    while n >= 1:
        # 3으로 나눈 나머지와 몫 구분, n은 다시 사용할수있게
        n, rest = divmod(n, 3)
        answer += str(rest)

    answer = int(answer, 3)

    return answer
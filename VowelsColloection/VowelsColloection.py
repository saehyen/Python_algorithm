def solution(word):
    # 각 알파벳마다 수 부여
    wordN = {'A':0,'E':1,'I':2,'O':3,'U':4}
    # 문자열로 자르기
    word = list(word)
    # maximum = 맥스값(3125)
    maximum = 5**5
    answer = 0
    # 문자열 규칙 = word숫자 * maximum(경우의 수) 나누기 4의 몫
    for i in word:
        answer += wordN[i]*(maximum-1)//4
        # 한자리수 이동마다 나누기5(경우의 수)
        maximum //= 5
    # 각자리수마다 걸리는 시간만큼 더해주기
    answer += len(word)
    return answer
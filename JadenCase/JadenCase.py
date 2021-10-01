# 테스트 불통과
def solution(s):
    answer = ""
    s_ = s.split()
    for i in s_ :
        for j in range(len(i)) :
            if j == 0 :
                answer = answer + i[j].upper()
            else:
                answer = answer + i[j].lower()
        if i != s_[-1]:
            answer += " "
    return answer
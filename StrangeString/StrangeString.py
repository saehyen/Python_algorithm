# 테스트는 통과했으나 틀린 답(1차시도)
def solution(s):
    s_ = s.split()
    answer = ""
    for i in s_:
        t = list(i)
        for j in range(len(t)) :
            if j %2 == 0:
                t[j] = t[j].upper()
            else :
                t[j] = t[j].lower()
            answer += t[j]
        answer += " "
    return answer.rstrip()


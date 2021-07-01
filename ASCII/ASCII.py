def solution(s, n):
    s = list(s)
    answer = ''
    for i in s:
        if ord(i) == 32 :
            answer += i
        else :
            i_ = ord(i)+n
            # i = 대문자
            if i_ > 90  and ord(i) < 91:
                i_ -= 26
            # i = 소문자
            elif ord(i) > 96 and i_ > 122:
                i_ -= 26
            else :
                i_ = i_
            # i = 대문자, i_ = 소문자구역 조건 = i < 90 and i_ > 97
            i_ = chr(i_)
            answer += i_
    return answer

def solution(a, b):
    sum = 0
    for i in range(1,a) :
        sum += month(i)
    sum += b
    answer = day(sum)
    return answer
# 달 기준 31 29 31 30 24
def month(c):
    if c == 1:
        sum = 31
    elif c == 2 :
        sum = 29
    elif c == 8 :
        sum = 31
    elif c == 9:
        sum = 30
    elif c == 10:
        sum = 31
    elif c == 11:
        sum = 30
    elif c == 12:
        sum = 31
    elif c % 2 == 1:
        sum = 31
    elif c % 2 == 0 :
        sum = 30
    return sum
# 일 기준
def day(sum) :
    if sum % 7 == 1 :
        return "FRI"
    if sum % 7 == 2 :
        return "SAT"
    if sum % 7 == 3 :
        return "SUN"
    if sum % 7 == 4 :
        return "MON"
    if sum % 7 == 5 :
        return "TUE"
    if sum % 7 == 6 :
        return "WED"
    if sum % 7 == 0 :
        return "THU"
def solution(dartResult):
    dartResult = dartResult.replace("10", "A")
    dartlist = list(dartResult)
    for i in range(len(dartlist)) :
        if dartlist[i] == "A" :
            dartlist[i] = 10
    answer = 0
    # 더블, 트리플 처리
    for i in range(len(dartlist)) :
        if dartlist[i] == "S" :
            dartlist[i-1] = int(dartlist[i-1])
        elif dartlist[i] == "D" :
            dartlist[i-1] = int(dartlist[i-1])**2
        elif dartlist[i] == "T" :
            dartlist[i-1] = int(dartlist[i-1])**3
    # 스타상, 아차상
    for i in range(len(dartlist)) :
        if dartlist[i] == "*" :
            dartlist[i-2] = 2*int(dartlist[i-2])
            if type(dartlist[i-4]) == int and i-4 >= 0:
                dartlist[i-4] = 2*int(dartlist[i-4])
            if dartlist[i-3] == "*" or dartlist[i-3] == "#" and type(dartlist[i-5]) == int and i-5 >= 0 :
                dartlist[i-5] = 2*int(dartlist[i-5])
        elif dartlist[i] == "#" and i-2 >= 0:
            dartlist[i-2] = -1*int(dartlist[i-2])
    # 연산 처리
    for i in range(len(dartlist)) :
        if type(dartlist[i]) == int :
            answer += dartlist[i]
            print(dartlist[i])
    return answer
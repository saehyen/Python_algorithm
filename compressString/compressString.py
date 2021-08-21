def solution(s):
    start = 0
    slist = []
    answerlist = [len(s)] * len(s)

    # 자르는 길이 : i
    for i in range(len(s)):
        plus = False
        plus2 = False
        # 자르는 구간 : j

        sl = []
        stack = []
        for j in range(int(len(s) / (i + 1))):
            sl.append(s[(i + 1) * j: (i + 1) * (j + 1)])
            if 1 < len(s) / (i + 1) - j < 2:
                sl.append(s[(i + 1) * (j + 1):])
        answer = 0
        # print(sl)
        for t in range(len(sl)):
            if len(stack) < 1:
                stack.append(sl[t])
                plu = 1
            elif stack[-1] != sl[t]:
                stack.append(sl[t])
                plu = 1
            # 같을 때
            elif stack[-1] == sl[t]:
                stack.append(sl[t])
                if len(stack) >= 3:
                    # 첫번째
                    if stack[-3] != stack[-1]:
                        answerlist[i] -= len(sl[t]) - 1
                        plu = 1
                    # 두번째이후
                    else:
                        answerlist[i] -= len(sl[t])
                        plu += 1
                        if 9 <= plu <= 98:
                            plus = True
                        elif 99 <= plu <= 998:
                            plus2 = True
                # 길이가 3개이상 되지 않으므로 무조건 -1
                else:
                    answerlist[i] -= len(sl[t]) - 1
                    plu = 1
        if plus == True:
            answerlist[i] += 1
        elif plus2 == True:
            answerlist[i] += 2
    slist.append(sl)
    # slist : 잘라진 리스트
    print(answerlist)
    return min(answerlist)
def solution(answers):
    ans1,ans2,ans3 = 0,0,0
    for i in range(len(answers)):
        # 1번 수포자의 조건
        if answers[i] == (i+1)%5:
            ans1 += 1
    for i in range(len(answers)):
        # 2번 수포자의 조건
        if i%2 == 0 and answers[i] == 2:
            ans2 += 1
        elif i%8 == 1 and answers[i] == 1:
            ans2 += 1
        elif i%8 == 3 and answers[i] == 3:
            ans2 += 1
        elif i%8 == 5 and answers[i] == 4:
            ans2 += 1
        elif i%8 == 7 and answers[i] == 5:
            ans2 += 1
    for i in range(len(answers)):
        # 3번 수포자의 조건
        if i%10 == 1 or i%10 == 2 and answers[i] == 3:
            ans3 += 1
        elif i%10 == 3 or i%10 == 4 and answers[i] == 1:
            ans3 += 1
        elif i%10 == 5 or i%10 == 6 and answers[i] == 2:
            ans3 += 1
        elif i%10 == 7 or i%10 == 8 and answers[i] == 4:
            ans3 += 1
        elif i%10 == 9 or i%10 == 0 and answers[i] == 5:
            ans3 += 1
    answer = []
    maxnum = max(ans1,ans2,ans3)
    if maxnum == ans1:
        answer.append(1)
    if maxnum == ans2:
        answer.append(2)
    if maxnum == ans3:
        answer.append(3)
    return answer
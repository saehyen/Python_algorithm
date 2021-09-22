def solution(N, stages):
    answer = []
    answer2 = []
    answer3 = []
    # stages.sort()
    num = len(stages)
    for i in range(1,N+1) :
        answer.append(stages.count(i))
    for j in range(len(answer)) :
        answer2.append([j+1,answer[j]/num])
        num -= answer[j]
    answer2.sort(key = lambda x:-x[1])
    for a2 in answer2 :
        answer3.append(a2[0])
    return answer3
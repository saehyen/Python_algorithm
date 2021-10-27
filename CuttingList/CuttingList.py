# 시간초과 답
def solution(n, left, right):
    index=1
    answerlist=[]
    lst= list(range(1,n+1))
    # n보다 인덱스가 작은 동안
    for i in range(1,n+1) :
        for j in range(i):
            lst[j] = i
        answerlist+= lst
    return answerlist[left:right+1]
            